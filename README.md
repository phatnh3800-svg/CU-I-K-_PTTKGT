# Tối ưu hóa bài toán đổi tiền và ứng dụng thực tế

## Thông tin đề tài

- Tên đề tài: Tối ưu hóa bài toán đổi tiền và ứng dụng thực tế
- Nội dung: So sánh cách tiếp cận bằng thuật toán Tham lam và Quy hoạch động cho bài toán đổi tiền với các bộ mệnh giá khác nhau.
- Mục tiêu: Phân tích điều kiện để giải thuật Tham lam cho kết quả tối ưu toàn cục.

# So sánh thuật toán Tham lam và Quy hoạch động trong bài toán đổi tiền

## 1. Giới thiệu đề tài

Đề tài xây dựng chương trình giải bài toán đổi tiền với mục tiêu tìm số lượng tờ tiền hoặc đồng xu ít nhất để tạo thành một số tiền cho trước.

Chương trình sử dụng và so sánh hai phương pháp:
- Thuật toán Tham lam (Greedy)
- Thuật toán Quy hoạch động (Dynamic Programming - DP)

Thông qua các bộ dữ liệu kiểm thử, chương trình cho thấy:
- Khi nào thuật toán Tham lam cho kết quả tối ưu
- Khi nào thuật toán Tham lam thất bại do rơi vào tối ưu cục bộ
- Quy hoạch động luôn tìm được lời giải tối ưu nếu tồn tại
- So sánh thời gian thực thi giữa hai phương pháp

---

## 2. Mục tiêu của chương trình

- Xây dựng chương trình bằng ngôn ngữ Python
- Tổ chức code theo từng file riêng để thuận tiện chỉnh sửa, kiểm tra và tổng hợp
- Lưu trữ và quản lý source code trên GitHub
- Tìm số lượng đồng tiền/tờ tiền ít nhất để đổi một số tiền cho trước
- So sánh độ chính xác của thuật toán Tham lam và Quy hoạch động
- Đánh giá hiệu năng của hai thuật toán trên nhiều bộ dữ liệu khác nhau
- Minh họa sự khác nhau giữa tối ưu cục bộ và tối ưu toàn cục
- Phân tích điều kiện để thuật toán Tham lam đạt được tối ưu toàn cục

---

## 3. Phân công nhiệm vụ nhóm

### Giai đoạn 1: Triển khai code

- Hải Nam: Chỉnh sửa và hỗ trợ code Quy hoạch động
- Quỳnh Như: Viết hàm thuật toán Quy hoạch động
- Tài: Tạo test case
- Minh Phúc: Viết hàm thuật toán Tham lam
- Sơn: Viết hàm so sánh hiệu năng và hàm Main
- Phát: Chỉnh sửa và tổng hợp code

### Giai đoạn 2: Làm nội dung và slide thuyết trình

- Hải Nam: Thuyết trình, tìm phần cơ sở lý thuyết và mở đầu
- Quỳnh Như: Tìm hiểu thuật toán Quy hoạch động, chụp source code và giải thích
- Minh Phúc: Tìm hiểu thuật toán Tham lam, chụp source code và giải thích
- Tài: Làm slide, chụp kết quả thử nghiệm, đánh giá thuật toán và nghiên cứu điều kiện để Greedy tối ưu toàn cục
- Sơn: Viết nhận xét so sánh hiệu năng hai thuật toán
- Phát: Tổng hợp nội dung, tìm hiểu điều kiện Greedy tối ưu toàn cục, viết kết luận và hướng phát triển

---

## 4. Cấu trúc thư mục

```text
.
├── __init__.py
├── main.py
├── input.py
├── greedy.py
├── dynamic_programming.py
├── compare_performance.py
├── test_case.py
└── README.md
```

---

## 5. Chức năng của từng file

### `greedy.py`
Chứa thuật toán Tham lam.

Ý tưởng:
- Luôn chọn mệnh giá lớn nhất có thể sử dụng
- Tiếp tục giảm dần cho đến khi đổi hết số tiền

Ưu điểm:
- Chạy rất nhanh
- Dễ cài đặt
- Hiệu quả với hệ thống tiền chuẩn như tiền Mỹ hoặc tiền Việt Nam

Nhược điểm:
- Không phải lúc nào cũng cho kết quả tối ưu
- Có thể rơi vào tối ưu cục bộ

---

### `dynamic_programming.py`
Chứa thuật toán Quy hoạch động.

Ý tưởng:
- Xây dựng lời giải tối ưu cho mọi số tiền từ 0 đến amount
- Sử dụng mảng `dp[i]` để lưu số đồng tiền ít nhất cần dùng cho số tiền `i`
- Dùng mảng `trace[i]` để truy vết các đồng tiền đã chọn

Ưu điểm:
- Luôn tìm được lời giải tối ưu nếu tồn tại
- Phù hợp với mọi hệ thống mệnh giá

Nhược điểm:
- Tốn nhiều bộ nhớ hơn
- Thời gian chạy chậm hơn khi amount lớn

---

### `compare_performance.py`
Dùng để:
- Chạy cả hai thuật toán trên cùng một bộ dữ liệu
- Đo thời gian thực thi của từng thuật toán
- Hiển thị kết quả dưới dạng bảng

---

### `test_case.py`
Chứa các bộ kiểm thử mẫu nhằm minh họa nhiều trường hợp khác nhau:

1. Greedy tối ưu
2. Greedy thất bại
3. Greedy thất bại rõ rệt
4. Ứng dụng thực tế với tiền Việt Nam
5. Trường hợp nhỏ
6. Trường hợp không có lời giải
7. Kiểm tra hiệu suất với dữ liệu lớn

---

### `main.py`
File chính dùng để:
- Đọc danh sách test case
- Chạy so sánh giữa Greedy và DP
- In kết quả ra màn hình

---

### `input.py`
Cho phép người dùng:
- Tự nhập danh sách mệnh giá
- Nhập số tiền cần đổi
- So sánh kết quả giữa hai thuật toán với dữ liệu do người dùng cung cấp

---

## 6. Nguyên lý hoạt động của các thuật toán

### Thuật toán Tham lam

Các bước thực hiện:
1. Sắp xếp mệnh giá theo thứ tự giảm dần
2. Chọn đồng tiền lớn nhất có thể dùng
3. Trừ dần khỏi số tiền cần đổi
4. Lặp lại cho đến khi hết tiền hoặc không thể đổi tiếp

Ví dụ:
- Mệnh giá: [1, 5, 10, 25]
- Số tiền: 63

Greedy chọn:
- 25 + 25 + 10 + 1 + 1 + 1
- Tổng cộng: 6 đồng

---

### Thuật toán Quy hoạch động

Các bước thực hiện:
1. Khởi tạo mảng `dp`
2. Với mỗi số tiền từ 1 đến amount:
   - Thử từng mệnh giá
   - Chọn cách có số lượng đồng tiền ít nhất
3. Truy vết lại lời giải từ mảng `trace`

Ví dụ:
- Mệnh giá: [1, 3, 4]
- Số tiền: 6

Greedy:
- 4 + 1 + 1 = 3 đồng

DP:
- 3 + 3 = 2 đồng

=> Quy hoạch động tối ưu hơn.

---

## 7. Độ phức tạp thuật toán

### Thuật toán Tham lam

- Thời gian: O(n)
- Bộ nhớ: O(k)

Trong đó:
- n là số lượng mệnh giá
- k là số đồng tiền được chọn

---

### Thuật toán Quy hoạch động

- Thời gian: O(amount × n)
- Bộ nhớ: O(amount)

Trong đó:
- amount là số tiền cần đổi
- n là số lượng mệnh giá

---

## 8. Các trường hợp kiểm thử tiêu biểu

### Test 1: Hệ thống tiền chuẩn
- Coins: [1, 5, 10, 25]
- Amount: 63
- Kết quả: Greedy và DP đều tối ưu

### Test 2: Greedy thất bại
- Coins: [1, 3, 4]
- Amount: 6
- Greedy: 4 + 1 + 1 = 3 đồng
- DP: 3 + 3 = 2 đồng

### Test 3: Greedy thất bại rõ rệt
- Coins: [1, 15, 25]
- Amount: 30
- Greedy: 25 + 1 + 1 + 1 + 1 + 1 = 6 đồng
- DP: 15 + 15 = 2 đồng

### Test 4: Trường hợp không có lời giải
- Coins: [5, 7]
- Amount: 11
- Không thể đổi chính xác

### Test 5: Dữ liệu lớn
- Coins: [1, 2, 5, 10, 20]
- Amount: 100000
- Greedy chạy gần như tức thời
- DP chậm hơn do phải xét toàn bộ các giá trị từ 1 đến 100000

---

## 9. Điều kiện để thuật toán Tham lam cho kết quả tối ưu toàn cục

Thuật toán Tham lam không phải lúc nào cũng tối ưu. Tuy nhiên, trong một số hệ thống mệnh giá đặc biệt, Greedy vẫn cho ra lời giải tốt nhất.

Greedy thường đạt tối ưu toàn cục khi:

- Hệ thống tiền là hệ thống chuẩn (Canonical Coin System)
- Mỗi mệnh giá lớn có thể được biểu diễn hiệu quả từ các mệnh giá nhỏ hơn
- Việc chọn đồng tiền lớn nhất trước không làm mất đi khả năng tạo ra lời giải ít đồng tiền nhất

Ví dụ các hệ thống mà Greedy hoạt động tốt:
- [1, 5, 10, 25]
- [1000, 2000, 5000, 10000, 20000, 50000]

Ví dụ hệ thống mà Greedy thất bại:
- [1, 3, 4] với amount = 6
- [1, 15, 25] với amount = 30

Do đó, trước khi áp dụng Greedy vào thực tế, cần kiểm tra xem hệ thống mệnh giá có phải là hệ thống chuẩn hay không.

---

## 10. Hướng dẫn chạy chương trình

### Chạy các test case có sẵn

```bash
python main.py
```

### Nhập dữ liệu từ bàn phím

```bash
python input.py
```

Ví dụ nhập:

```text
Nhập các mệnh giá tiền: 1,3,4
Nhập số tiền cần đổi: 6
```

---

## 11. Kết luận

Qua chương trình có thể thấy:

- Thuật toán Tham lam rất nhanh và phù hợp với các hệ thống tiền chuẩn
- Tuy nhiên, Tham lam không đảm bảo luôn tìm được lời giải tối ưu
- Quy hoạch động tuy chậm hơn nhưng luôn tìm được đáp án tốt nhất
- Trong các bài toán yêu cầu độ chính xác tuyệt đối, Quy hoạch động là lựa chọn phù hợp hơn
- Trong các bài toán cần tốc độ cao và dữ liệu phù hợp, Tham lam là phương án hiệu quả
- Qua quá trình thực hiện đề tài, nhóm nhận thấy rằng việc lựa chọn thuật toán phụ thuộc vào mục tiêu của bài toán. Nếu cần tốc độ xử lý nhanh trong hệ thống mệnh giá chuẩn thì Greedy là lựa chọn phù hợp. Nếu cần đảm bảo tối ưu tuyệt đối trong mọi trường hợp thì nên sử dụng Quy hoạch động.

---

## 12. Kiến thức áp dụng

Đề tài áp dụng các kiến thức của học phần Phân tích thiết kế giải thuật:
- Phân tích độ phức tạp thuật toán
- Thuật toán Tham lam
- Quy hoạch động
- So sánh hiệu năng giữa các giải thuật
- Đánh giá tính tối ưu của lời giải
- Thiết kế bộ kiểm thử cho nhiều trường hợp khác nhau

