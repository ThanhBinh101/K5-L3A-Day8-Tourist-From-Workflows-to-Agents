# Team

## Thông tin nhóm

- Tên nhóm:
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY08-TenNhom-FromWorkflowsToAgents` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt:

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Nguyễn Thị Hồng San | 2A202603513 | 26ai.sannth@vinuni.edu.vn | nhánh `03513-NguyenThiHongSan` | workflow (shape A) |
|   2 |        |      |       |        |         |

Gợi ý chia vai:

- Nhóm 6 người: integration; workflow; single agent; orchestrator; ledger/policy/crash; eval/report.
- Nhóm 4 người: workflow + integration; single; orchestrator + handoff; ledger + evaluation.

## Bảng đóng góp

`python -m lab8.check_submission` đọc bảng này bằng máy: giữ nguyên tiêu đề `## Bảng đóng góp` và các cột. Mỗi người một dòng: commit có nội dung và ít nhất một test đã thêm hoặc sửa.

| Người | Vai | Commit | Test đã thêm hoặc sửa |
| --- | --- | --- | --- |
| Nguyễn Thị Hồng San | workflow (shape A) | `aae7ba2`, `2a26331`, `0314734` | `src/tests/test_workflow_shape.py` (107 test) |

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## MSSV_HoTen

### Phần việc phụ trách

-

### Đóng góp cụ thể

-

### Bằng chứng

-

## 2A202603513_NguyenThiHongSan

### Phần việc phụ trách

- Shape A — workflow (`src/lab8/shapes/workflow.py`) và các phần CP3–CP4 của shape này: crash, ledger, approval, secret.

### Đóng góp cụ thể

- `aae7ba2`: viết shape workflow (CP2).
- `2a26331`: làm cứng workflow (không ném exception, `order_id` trắng → `needs_info`), thêm `reports/crash.json` (20/20).
- `0314734`: thêm `src/tests/test_workflow_shape.py`, 107 test trong cổng host.

### Bằng chứng

- Ma trận student workflow: 62 passed. Cổng host: 161 passed. Crash suite: 20/20.
- Benchmark public 5 seed: pass 1.000, pass^5 1.000, cost/success 35.30 VND (mô phỏng).
- Báo cáo chi tiết: [report/team/2A202603513_NguyenThiHongSan.md](report/team/2A202603513_NguyenThiHongSan.md).
