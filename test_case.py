def get_test_cases():
    return [

        # 1. GREEDY TỐI ƯU (Hệ thống tiền chuẩn - Canonical)
        {
            "id": 1,
            "name": "Greedy tối ưu (đồng xu Mỹ)",
            "coins": [1, 5, 10, 25],
            "amount": 63,
            "purpose": "Greedy optimal (Standard system)",
            "expected_note": "Greedy: 2x25 + 1x10 + 3x1 = 6 coins"
        },

        # 2. GREEDY SAI (Bẫy tối ưu cục bộ - Non-canonical)
        {
            "id": 2,
            "name": "Greedy sai (bẫy tối ưu cục bộ)",
            "coins": [1, 3, 4],
            "amount": 6,
            "purpose": "Greedy falls into local optimum",
            "expected_note": "Greedy: 4+1+1 (3 tờ) | DP: 3+3 (2 tờ)"
        },

        # 3. GREEDY SAI RÕ RỆT (Sai số lớn)
        {
            "id": 3,
            "name": "Greedy sai rõ rệt (sai số lớn)",
            "coins": [1, 15, 25],
            "amount": 30,
            "purpose": "Demonstrate large discrepancy in coin count",
            "expected_note": "Greedy: 25+1*5 (6 tờ) | DP: 15+15 (2 tờ)"
        },

        # 4. ỨNG DỤNG THỰC TẾ (Tiền Việt Nam)
        {
            "id": 4,
            "name": "Ứng dụng thực tế tiền Việt Nam",
            "coins": [1000, 2000, 5000, 10000, 20000, 50000],
            "amount": 98000,
            "purpose": "Verify algorithms with real-world denominations",
            "expected_note": "Both should return optimal 6 coins (50+20+20+5+2+1)"
        },

        # 5. TRƯỜNG HỢP NHỎ (Kiểm tra điều kiện biên)
        {
            "id": 5,
            "name": "Trường hợp nhỏ kiểm tra điều kiện ",
            "coins": [1, 2, 5],
            "amount": 3,
            "purpose": "Simple input validation",
            "expected_note": "Optimal: 2+1 (2 tờ)"
        },

        # 6. KHÔNG CÓ LỜI GIẢI (Edge Case)
        {
            "id": 6,
            "name": "Trường hợp không có lời giải",
            "coins": [5, 7],
            "amount": 11,
            "purpose": "Test error handling (Target cannot be reached)",
            "expected_note": "Should return None"
        },

        # 7. TEST HIỆU NĂNG (Dữ liệu lớn)
        {
            "id": 7,
            "name": "Test hiệu năng với dữ liệu lớn",
            "coins": [1, 2, 5, 10, 20],
            "amount": 100000, 
            "purpose": "Measure execution time difference (DP vs Greedy)",
            "expected_note": "Greedy will be nearly 0s, DP will take measurable time"
        }
    ]


