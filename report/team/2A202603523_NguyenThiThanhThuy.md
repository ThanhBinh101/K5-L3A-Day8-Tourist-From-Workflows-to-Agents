# Báo cáo cá nhân — Nguyễn Thị Thanh Thúy

File được đặt theo quy tắc `MSSV_HoTen.md`.

## 1. Thông tin thành viên

- Họ tên: Nguyễn Thị Thanh Thúy
- MSSV: 2A202603523
- Email: thanhthuy02072004@gmail.com (theo Git config của workspace)
- GitHub: Chưa xác minh; Git author name trong workspace là `Thuydesign`, chưa đủ căn cứ xác nhận username.

## 2. Phần việc phụ trách

Phụ trách hoàn thiện ba shape nhóm viết và kiểm chứng các mốc CP3–CP5: `workflow`, `single`, `orchestrator`; chạy crash/retry, handoff safety, benchmark public và tổng hợp báo cáo. Vai trò được ghi theo yêu cầu của thành viên trong phiên này.

## 3. Đóng góp cụ thể

Chưa có commit mới; HEAD trước các thay đổi là `034c6c4`. Không thêm/sửa test; đã chạy test hiện có: student matrix 248 passed, host suite 54 passed. Quyết định kỹ thuật: truyền quote đầy đủ cho host, chuyển tiếp crash injection, dùng handoff read-only đã sanitize và chọn workflow theo benchmark public vì cùng pass rate nhưng cost thấp nhất.

## 4. Bằng chứng

`src/reports/crash.json` (`20/20`); `src/reports/benchmark.json`; run id mẫu `R-workflow-C-001-s11`; kiểm thử `tests/test_public_matrix.py` (248 passed), host suite (54 passed) và `python -m lab8.check_submission`. Check submission hiện còn báo thiếu thông tin đóng góp trong `TEAM.md` ở lần kiểm trước khi điền mục này; cần chạy lại sau khi hoàn tất.

## 5. Công cụ AI đã dùng

Đã dùng AI assistant using Copilot SDK in VS Code để hỗ trợ đọc contract, triển khai code, chạy kiểm tra và tổng hợp report. Không dùng API/model thật cho lab. Kết quả được tự kiểm bằng student matrix, host suite, smoke, crash suite và benchmark do lab sinh; các lệnh và kết quả được ghi trong báo cáo nhóm. Xem [RULES.md](../../RULES.md).

## 6. Tự đánh giá

Hoàn thành triển khai và kiểm tra trên phạm vi public; các shape nhóm viết đạt 100% trên benchmark 14 claim × 5 seed, crash suite đạt 20/20, host suite và student matrix đều xanh. Hạn chế còn lại là chưa chạy hidden grader, chưa có commit chứa thay đổi và GitHub username chưa xác minh; cần bổ sung các mục này trước khi nộp.
