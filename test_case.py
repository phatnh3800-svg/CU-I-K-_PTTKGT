def get_test_cases():
    return [

        # 1. GREEDY TỐI ƯU (Hệ thống tiền chuẩn - Canonical)
        {
            "id": 1,
            "name": "Tiền xu Mỹ",
            "coins": [1, 5, 10, 25],
            "amount": 63,
            "purpose": "Thuật toán Tham lam được tối ưu",
            
        },

        # 2. GREEDY SAI (Bẫy tối ưu cục bộ - Non-canonical)
        {
            "id": 2,
            "name": "Thất bại Tham lam hay gặp",
            "coins": [1, 3, 4],
            "amount": 6,
            "purpose": "Thuật toán tham lam rơi vào điểm tối ưu cục bộ.",
           
        },

        # 3. GREEDY SAI RÕ RỆT (Sai số lớn)
        {
            "id": 3,
            "name": "Thất bại Tham lam rõ rệt",
            "coins": [1, 15, 25],
            "amount": 30,
            "purpose": "Thể hiện sự chênh lệch lớn trong số lượng tiền.",
            
        },

        # 4. ỨNG DỤNG THỰC TẾ (Tiền Việt Nam)
        {
            "id": 4,
            "name": "Tiền Việt Nam",
            "coins": [1000, 2000, 5000, 10000, 20000, 50000],
            "amount": 98000,
            "purpose": "Kiểm chứng thuật toán với các mệnh giá thực tế.",
            
        },

        # 5. TRƯỜNG HỢP NHỎ (Kiểm tra điều kiện biên)
        {
            "id": 5,
            "name": "Trương hợp nhỏ",
            "coins": [1, 2, 5],
            "amount": 3,
            "purpose": "Xác thực đầu vào đơn giản",
            
        },

        # 6. KHÔNG CÓ LỜI GIẢI (Edge Case)
        {
            "id": 6,
            "name": "Trường hợp bất khả thi",
            "coins": [5, 7],
            "amount": 11,
            "purpose": "Xử lý lỗi kiểm thử (Không thể đạt mục tiêu)",
            
        },

        # 7. TEST HIỆU NĂNG (Dữ liệu lớn)
        {
            "id": 7,
            "name": "Kiểm tra hiệu suất",
            "coins": [1, 2, 5, 10, 20],
            "amount": 100000, 
            "purpose": "Thời gian Greedy gần bằng 0, còn DP mất một khoảng thời gian mới đo được.",
            
        }
    ]