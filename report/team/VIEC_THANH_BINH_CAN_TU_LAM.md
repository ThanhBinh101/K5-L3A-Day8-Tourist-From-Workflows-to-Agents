# Những việc Thanh Bình cần tự làm trước khi nộp

Báo cáo cá nhân đã được soạn đầy đủ ở `2A202603497_NguyenThiThanhBinh.md`, gồm mục tiêu, giải pháp, khó khăn, kết quả, khai báo AI và đánh giá kỹ thuật. Những việc dưới đây cần thao tác hoặc thông tin thực của bạn; chưa được đánh dấu hoàn thành thay cho bạn.

## 1. Xác nhận thông tin và đọc lại báo cáo

- [ ] Kiểm tra họ tên Nguyễn Thị Thanh Bình, MSSV 2A202603497, lớp L3A, nhóm Tourist và GitHub ThanhBinh101.
- [ ] Đọc mục 2–3 và xác nhận phần việc được ghi đúng với thực tế phân công nhóm. Không nhận implementation workflow/orchestrator là tự viết nếu không phụ trách.
- [ ] Giữ khai báo Codex ở mục 5. Nếu còn dùng công cụ khác, bổ sung đúng tên và phạm vi hỗ trợ.

Không tự thêm email hoặc thành viên khác khi chưa có dữ liệu xác nhận. Báo cáo hiện giữ thông tin theo bản bạn đã chỉnh.

## 2. Tự chạy test và xem kết quả

Mở Terminal, chạy:

```bash
cd /Users/eroheta/Documents/K5-Day8-Tourist-From-Workflows-to-Agents/src
python3 -m pytest -q -m student -o addopts= -k 'single and not workflow and not orchestrator and not swarm'
python3 -m pytest -q tests/test_demo_web.py
```

Kết quả đã đo ở snapshot hiện tại: lệnh đầu **62 passed**, lệnh thứ hai **15 passed**. Số deselected hoặc tổng test có thể thay đổi khi nhóm thêm test; điều quan trọng là không có fail mới.

- [ ] Tự thực hiện hai lệnh và đọc lỗi nếu có.
- [ ] Nếu kết quả khác báo cáo, đối chiếu phiên bản code và hỏi nhóm; không sửa số trong JSON cho khớp.

Các lần chạy trước trong báo cáo là do Codex thực hiện. Sau khi bạn tự chạy, có thể bổ sung vào mục 5 ngày chạy, lệnh và kết quả thật; không ghi trước rằng đã tự kiểm tra.

## 3. Tự demo trong khoảng 5 phút

Khởi động server từ thư mục src:

```bash
python3 -m lab8.demo.web --port 8088
```

Mở [http://127.0.0.1:8088](http://127.0.0.1:8088). Dừng server bằng Ctrl+C sau khi dùng.

| Lần thử | Thao tác | Cần tự thấy và giải thích |
|---|---|---|
| 1 | C-001, Chạy một lần | Cả ba resolved; quote/effect 35.000đ; 1 refund, 1 audit |
| 2 | C-002 | denied, không refund: order trễ 2 ngày dù ticket nói 5 ngày |
| 3 | C-007 | Quote 35.000đ nhưng host chặn vì approval không hợp lệ |
| 4 | C-008 | Quote 35.000đ nhưng effect chỉ 20.000đ do approval |
| 5 | C-014 | Quote 150.000đ, effect mới 120.000đ vì trước đó trả 30.000đ |
| 6 | C-001, Chạy lại cùng claim | Hai lượt chạy nhưng vẫn chỉ 1 refund, không trả thêm |
| 7 | Crash → phục hồi | Lượt đầu crashed, lượt hai resolved; tổng effect của claim vẫn 35.000đ |

- [ ] Thử các tình huống và mở tab Single Agent để đọc trace.
- [ ] Tự giải thích bằng lời của mình, không chỉ đọc các con số trên card.

## 4. Những câu có thể bị hỏi khi bảo vệ

Đây là gợi ý kiến thức để bạn luyện, không phải xác nhận bạn đã hiểu:

1. **Single khác workflow ở đâu?** Workflow đi theo checklist cố định; single dùng vòng decide → tool → observation, tối đa 8 lượt. Tuy nhiên MockLLM của đề chưa có tool-calling thật, nên callback vẫn được viết bằng code.
2. **Ai tính và ai ghi tiền?** compute_compensation tính quote; host issue_refund kiểm approval/cap/idempotency và ghi ledger. Agent chỉ có tool đọc trong vòng ReAct.
3. **Vì sao gửi quote đầy đủ?** Host là nơi trừ tiền đã trả. Shape tự trừ trước sẽ gây trừ hai lần.
4. **Vì sao crash không trả trùng?** Refund gắn với khóa refund:claim_id trong ledger. Sau crash, host nhận ra effect đã có và replay thay vì ghi thêm.
5. **Không log field nào?** Không log ticket, parent_secret, raw_headers, phone/address/item/internal_note. Trace chỉ giữ dữ liệu cần thiết đã qua ranh giới chọn field.
6. **62 test và 70 trial khác gì?** 62 là ma trận test riêng của shape; benchmark có 14 claim × 5 seed = 70 trial. Không cộng chúng thành số claim khác nhau.
7. **Tại sao không kết luận single luôn rẻ nhất?** MockLLM là mô phỏng; prompt và cách đếm tool khác nhau giữa implementation. Public nhỏ, chưa có hidden.

- [ ] Chọn hai điểm bạn còn chưa rõ và hỏi/đọc lại code đến khi tự giải thích được.

## 5. Tự bổ sung trải nghiệm thật vào phần đánh giá

Mục 6 trong báo cáo đã có đánh giá sản phẩm và bài học kỹ thuật dựa trên bằng chứng. Sau khi làm mục 2–4 ở trên, bạn nên thêm một đoạn ngắn (khoảng 4–6 câu) mô tả trải nghiệm thật:

- Bạn đã tự chạy tình huống nào và kết quả gì?
- Chỗ nào ban đầu chưa hiểu, sau đó đã hiểu hơn?
- Bạn đã tự chỉnh, kiểm tra hoặc bổ sung test nào?
- Bạn còn cần cải thiện điều gì?

Không có đoạn tự thuật viết sẵn để bạn nhận là trải nghiệm thật. Nếu phần lớn code được AI hỗ trợ, cứ ghi đúng phạm vi hỗ trợ và cách bạn kiểm chứng.

## 6. Test, commit và bảng đóng góp

- [ ] Đọc ít nhất một test trong `src/tests/test_demo_web.py`, hiểu input, expected và vì sao test phát hiện được lỗi. Tự điều chỉnh hoặc thêm trường hợp phù hợp nếu có phần còn thiếu; không thêm test vô nghĩa chỉ để đủ số.
- [ ] Sau khi review, tạo commit cho phần UI/test/báo cáo được nhóm chấp thuận, giữ nguyên khai báo AI. Commit `1ce29a9` chỉ có single.py, chưa chứng minh có test mới.
- [ ] Ghi commit/test thật của bạn vào TEAM.md và cập nhật mục 4.1 báo cáo cá nhân. Không nhận toàn bộ 442 test của repo là test tự viết.
- [ ] Đồng bộ với nhóm trước khi chốt: main hiện đang có thay đổi local và đã quan sát thấy chậm hơn origin/main; không force-push hoặc tự reset để xử lý.

Codex có thể hỗ trợ Git khi bạn yêu cầu; phần bạn cần làm là review và xác nhận đúng đóng góp thực. Chưa tự commit/push thay đổi mới trong lượt viết báo cáo này.

## 7. Việc nộp bài của nhóm và cá nhân

- [ ] Nhóm hoàn tất TEAM.md, decision_adr.md, research_card.md, báo cáo các thành viên và commit chốt. Báo cáo cá nhân đầy đủ không thay thế các mục này.
- [ ] Chạy `python3 -m lab8.check_submission` từ src sau khi điền đủ tài liệu; cần 0 FAIL. Lần kiểm trước vẫn còn lỗi tài liệu nhóm, không phải lỗi chạy shape.
- [ ] Nhóm push lên repo mà giảng viên truy cập được; kiểm file báo cáo cá nhân xuất hiện trên GitHub.
- [ ] **Bạn tự nộp link repo nhóm lên LMS bằng tài khoản của mình.** Theo SUBMISSION.md, nhóm đã push không thay thế việc mỗi thành viên tự nộp link.
