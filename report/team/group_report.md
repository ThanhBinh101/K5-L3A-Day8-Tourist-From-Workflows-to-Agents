# Báo cáo nhóm — Lab 8 LogiX-VN

Tối đa 5 trang ngoài phụ lục. Số liệu lấy từ file trong `src/reports/`, không chép tay từ terminal.

## 1. Thông tin nhóm

- Tên nhóm: Chưa được cung cấp; xem thông tin nhóm trong `TEAM.md`.
- Thành viên: Chưa được khai báo trong `TEAM.md`; chưa thể xác nhận danh sách.
- Commit chốt (trùng `report/team/decision_adr.md`): Chưa commit; working tree dựa trên HEAD `034c6c4`.

## 2. Mục tiêu và cách tiếp cận

Bài toán yêu cầu cùng một claims flow chạy trên bốn shape, với nguồn sự thật là order/policy và quyền ghi refund chỉ thuộc host. Mỗi shape đọc claim/order qua tool allowlist, dùng `compute_compensation` để tính quote, rồi chỉ chuyển quote đầy đủ sang `durability.issue_refund`; host kiểm approval, cap theo order, idempotency và ledger. Ba shape nhóm viết được triển khai theo thứ tự workflow xác định, single ReAct có giới hạn 8 bước, rồi orchestrator handoff cho investigator chỉ đọc. Thông tin phân công thành viên chưa được cung cấp.

## 3. Giải pháp

`workflow` đọc claim view, lookup order và tính quote bằng code; không để model quyết định tiền. `single` dùng `run_react` tối đa 8 bước để chọn các tool đọc, còn quote và refund vẫn do code/host xử lý. `orchestrator` tạo handoff bằng `make_handoff`, chỉ cấp read-only tools và trace handoff đã sanitize; investigator không thể ghi ledger. Trace ghi trạng thái lookup, quote, decision, handoff đã lọc và crash marker, nhưng không ghi ticket thô, parent secret, headers, SĐT, địa chỉ, ghi chú nội bộ hoặc tên hàng. Xem [docs/architecture.md](../../docs/architecture.md) và [docs/contracts.md](../../docs/contracts.md).

## 4. Kết quả

Benchmark `src/reports/benchmark.json`: 14 public claims × 5 seeds = 70 trial/shape. Cost là VND mô phỏng; variance là population variance của seed pass rate.

| Shape | Pass rate | Pass^5 | Seed min–max | Variance | Cost/success (VND) | Mean/p95 steps |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| workflow | 1.000 | 1.000 | 1.000–1.000 | 0.000000 | 27.86 | 3.79 / 4 |
| single | 1.000 | 1.000 | 1.000–1.000 | 0.000000 | 30.30 | 3.79 / 4 |
| orchestrator | 1.000 | 1.000 | 1.000–1.000 | 0.000000 | 55.71 | 4.71 / 5 |
| swarm | 0.986 | 0.929 | 0.929–1.000 | 0.000816 | 49.57 | 2.80 / 3 |

Swarm trượt 1 trial: C-002, seed 55, trả resolved thay vì denied do tin số ngày trong ticket. `src/reports/crash.json` báo `crash_safety = 20/20`; crash rồi resume giữ một refund và một audit. Không có `student_drop/` để tự kiểm hidden trong workspace này; hidden grader chưa chạy.

Quyết định kiến trúc và lý do: xem `report/team/decision_adr.md`. Phiếu nghiên cứu và ablation: xem `report/team/research_card.md`.

## 5. Khó khăn và cách xử lý

`python -m lab8.demo.buggy_workflow` in `unsafe refund rows: 2 (the host ledger must stay at 1)`, minh họa checkpoint đơn lẻ không ngăn trả trùng; nhóm dựa vào ledger/idempotency của host. `python -m lab8.crash_test --count 20 --out reports/crash.json` cho `crash_safety 20/20`. `python -m pytest -q -m student -o addopts=` cho 248 passed; `python -m pytest -q` cho 54 passed; `python -m lab8.smoke` in `lab8.smoke pass`. Các số liệu benchmark được lấy từ JSON do lệnh lab sinh ra.

## 6. Tổng hợp đóng góp

Thông tin cá nhân và phần việc của Nguyễn Thị Thanh Thúy được ghi trong `TEAM.md` và [báo cáo cá nhân](2A202603523_NguyenThiThanhThuy.md). Thông tin thành viên thứ hai chưa được cung cấp.

## 7. Hạn chế và hướng cải thiện

Kết quả chỉ phủ 14 public claims và 5 seed, không thay thế hidden set 40 × 5. MockLLM không phải model sản xuất, cost chỉ mô phỏng, latency là `unavailable`; không có dữ liệu `student_drop/` hoặc hidden grade. Kết luận chọn workflow cần được xem lại nếu hidden pass rate xuống dưới ngưỡng, có must-pass fail, hoặc đo model thật cho thấy latency/chi phí/nhu cầu song song làm shape khác phù hợp hơn.

## 8. Tài liệu tham khảo

1. Cemri et al. (2025), “Why Do Multi-Agent LLM Systems Fail?”, arXiv:2503.13657v3, https://arxiv.org/abs/2503.13657.
2. Tài liệu lab: [docs/business_rules.md](../../docs/business_rules.md), [docs/contracts.md](../../docs/contracts.md), [docs/metrics.md](../../docs/metrics.md), [CHECKPOINTS.md](../../CHECKPOINTS.md).
