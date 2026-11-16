# Team

## Thông tin nhóm

- Tên nhóm: Tourist
- Lớp: L3A
- Repo nhóm: `K5-L3A-Day8-Tourist-From-Workflows-to-Agents` (tên repo hiện tại)
- URL repo, nhánh nộp, commit chốt: https://github.com/ThanhBinh101/K5-L3A-Day8-Tourist-From-Workflows-to-Agents · main · code ceca05b3681429f7c7fa7843db215610c63019c7

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
| 1 | Nguyễn Thị Thanh Bình | 2A202603497 | Chưa cung cấp | ThanhBinh101 | Single ban đầu; UI demo/test/report, có hỗ trợ Codex |
| 2 | Lưu Đăng Tuấn | 2A202603454 | 26ai.tuanld@vinuni.edu.vn | kegacua | Crash trace và test single |
| 3 | Nguyễn Thị Hồng San | 2A202603513 | 26ai.sannth@vinuni.edu.vn | Nhánh 03513-NguyenThiHongSan | Workflow và test biên |
| 4 | Nguyễn Thành Danh | 2A202603493 | Theo báo cáo cá nhân | Nhánh 03493-NguyenThanhDanh | Orchestrator durability, benchmark |
| 5 | Võ Lê Hải Đăng | 2A202603577 | 910volehaidang2019@gmail.com | Hdang3825 | Orchestrator và security tests |
| 6 | Nguyễn Thị Thanh Thúy | 2A202603523 | 26ai.thuyntt@vinuni.edu.vn | Nhánh 03523-NguyenThiThanhThuy | Phương án ba shape, ADR/research/report |

Gợi ý chia vai:

- Nhóm 6 người: integration; workflow; single agent; orchestrator; ledger/policy/crash; eval/report.
- Nhóm 4 người: workflow + integration; single; orchestrator + handoff; ledger + evaluation.

## Bảng đóng góp

`python -m lab8.check_submission` đọc bảng này bằng máy: giữ nguyên tiêu đề `## Bảng đóng góp` và các cột. Mỗi người một dòng: commit có nội dung và ít nhất một test đã thêm hoặc sửa.

| Người | Vai | Commit | Test đã thêm hoặc sửa |
| --- | --- | --- | --- |
| Nguyễn Thị Thanh Bình | Single ban đầu; UI/test demo có hỗ trợ Codex | `1ce29a9`, `3c3f9b2`, `92a0753` | `src/tests/test_demo_web.py` (15 trường hợp; cần người học tự review theo khai báo AI) |
| Lưu Đăng Tuấn | Crash trace và test single | `bf6cb68` | `src/tests/test_single_shape.py` |
| Nguyễn Thị Hồng San | Workflow và kiểm thử biên | `aae7ba2`, `2a26331`, `0314734` | `src/tests/test_workflow_shape.py` (107 test) |
| Nguyễn Thành Danh | Orchestrator durability/benchmark | `2d6348f`, `e77ad2b` | `src/tests/test_orchestrator_durability.py` |
| Võ Lê Hải Đăng | Orchestrator/security | `a734b3d`, `13ae289` | `src/tests/test_orchestrator_security.py` |
| Nguyễn Thị Thanh Thúy | Phương án ba shape; ADR/research/report | `a1cf839`, `bd3941c`, `4bab90a` | Không thêm/sửa test; đã dùng test có sẵn theo báo cáo cá nhân — cần bổ sung nếu tiêu chí yêu cầu |

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
