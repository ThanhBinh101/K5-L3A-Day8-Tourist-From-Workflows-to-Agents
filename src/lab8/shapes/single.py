"""Shape B — one ReAct agent. Student work.

Use `lab8.runtime.run_react` with max_steps=8. `decide` may pick a read tool.
It must not call `issue_refund`. After the loop, the host validates the quote
and is the only writer.

A decide() that trusts ticket text over the order row will fail hidden claims
where the customer overstates the delay or cites a superseded clause.

Per-order cap: an order may already have been refunded by an earlier claim.
The read tool `lookup_refund_history` shows how much. The host still enforces
the cap, so pass the full quote to `durability.issue_refund`, not a net amount.

Caps: stop at 8 steps. Count model calls in the Budget so cost stays comparable.

Trace contract v1 (docs/contracts.md): return a trace_path to a JSON file written in this run,
{"run_id": <same run_id>, "events": [...]}, on every return path including early
ones. `lab8.trace.Trace` does this; your own tracer is fine if it matches.
"""

from __future__ import annotations

import sqlite3

from lab8.db import connect
from lab8.durability import InjectedCrash, issue_refund
from lab8.mock_llm import complete
from lab8.runtime import run_react
from lab8.schemas import Budget, RunResult, make_run_id
from lab8.shapes.common import finish
from lab8.tools import get_claim_view, tool_cost
from lab8.trace import Trace


def run_claim(
    claim_id: str,
    *,
    seed: int,
    store_path: str,
    crash_at: str | None = None,
) -> RunResult:
    conn = connect(store_path)
    try:
        return _run(conn, claim_id, seed=seed, crash_at=crash_at)
    finally:
        conn.close()


def _run(
    conn: sqlite3.Connection,
    claim_id: str,
    *,
    seed: int,
    crash_at: str | None,
) -> RunResult:
    budget = Budget()
    trace = Trace(make_run_id("single", claim_id, seed))
    budget.add_tool(tool_cost())
    claim = get_claim_view(conn, claim_id)
    trace.add("claim", {"found": claim["found"], "has_order_id": bool(claim.get("order_id"))})
    if not claim["found"]:
        trace.add("decision", {"status": "failed"})
        return finish(
            conn,
            shape="single",
            claim_id=claim_id,
            seed=seed,
            status="failed",
            proposal_amount=0,
            budget=budget,
            trace=trace,
            error_reason="unknown_claim",
        )
    if not claim.get("order_id"):
        trace.add("decision", {"status": "needs_info"})
        return finish(
            conn,
            shape="single",
            claim_id=claim_id,
            seed=seed,
            status="needs_info",
            proposal_amount=0,
            budget=budget,
            trace=trace,
            error_reason="missing_order_id",
        )

    observation = {
        "claim": {
            "claim_id": claim_id,
            "order_id": claim["order_id"],
            "principal_id": claim["principal_id"],
        }
    }

    def decide(seen: dict) -> dict:
        last_tool = seen.get("last_tool")
        result = seen.get("last_result", {})
        complete(
            budget,
            seed=seed,
            purpose="single_decision",
            prompt=(
                f"last_tool={last_tool or 'start'}; "
                f"visible={result.get('visible')}; "
                f"has_order={bool(result.get('order'))}; "
                f"has_quote={'amount_vnd' in result}"
            ),
        )
        if last_tool is None:
            return {
                "tool": "lookup_order",
                "args": {
                    "order_id": observation["claim"]["order_id"],
                    "principal_id": observation["claim"]["principal_id"],
                },
            }
        if last_tool == "lookup_order":
            if not result.get("visible"):
                return {
                    "final": {
                        "status": "escalated",
                        "proposal_amount": 0,
                        "error_reason": result.get("reason"),
                    }
                }
            return {"tool": "compute_compensation", "args": {"order": result["order"]}}
        if last_tool == "compute_compensation":
            amount = int(result["amount_vnd"])
            return {
                "final": {
                    "status": "denied" if amount <= 0 else "quoted",
                    "proposal_amount": amount,
                    "error_reason": result.get("reason") if amount <= 0 else None,
                }
            }
        return {
            "final": {
                "status": "failed",
                "proposal_amount": 0,
                "error_reason": "unexpected_tool",
            }
        }

    reacted = run_react(conn, budget, observation=observation, decide=decide, max_steps=8)
    final = reacted["final"]
    if reacted["stopped"] == "step_cap":
        trace.add("decision", {"status": "failed", "reason": "step_cap"})
        return finish(
            conn,
            shape="single",
            claim_id=claim_id,
            seed=seed,
            status="failed",
            proposal_amount=0,
            budget=budget,
            trace=trace,
            error_reason="step_cap",
        )
    if final["status"] == "escalated":
        trace.add("order_lookup", {"visible": False, "reason": final["error_reason"]})
        trace.add("decision", {"status": "escalated"})
        return finish(
            conn,
            shape="single",
            claim_id=claim_id,
            seed=seed,
            status="escalated",
            proposal_amount=0,
            budget=budget,
            trace=trace,
            error_reason=final["error_reason"],
        )

    quote = reacted["observation"]["last_result"]
    if final["status"] == "failed":
        trace.add("decision", {"status": "failed", "reason": final["error_reason"]})
        return finish(
            conn,
            shape="single",
            claim_id=claim_id,
            seed=seed,
            status="failed",
            proposal_amount=0,
            budget=budget,
            trace=trace,
            error_reason=final["error_reason"],
        )

    trace.add("order_lookup", {"visible": True, "reason": "ok"})
    trace.add("quote", quote)
    proposal = int(final["proposal_amount"])
    if final["status"] == "denied":
        trace.add("decision", {"status": "denied"})
        return finish(
            conn,
            shape="single",
            claim_id=claim_id,
            seed=seed,
            status="denied",
            proposal_amount=0,
            budget=budget,
            trace=trace,
            error_reason=final["error_reason"],
        )

    try:
        outcome = issue_refund(conn, claim_id, proposal, crash_at=crash_at)
    except InjectedCrash:
        trace.add("crash", {"at": crash_at})
        trace.write()
        raise

    status = "resolved" if outcome["ok"] else ("failed" if outcome["conflict"] else "denied")
    trace.add("decision", {"status": status, "reason": outcome["reason"]})
    return finish(
        conn,
        shape="single",
        claim_id=claim_id,
        seed=seed,
        status=status,
        proposal_amount=proposal,
        budget=budget,
        trace=trace,
        error_reason=None if outcome["ok"] else outcome["reason"],
    )
