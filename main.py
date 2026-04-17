from test_case import get_test_cases
from compare_performance import compare_performance
def main():
    test_cases = get_test_cases()
    
    # In tiêu đề bảng
    header = f" {'ID':<3} | {'Tên':<25} | {'Mệnh giá':<40} | {'Tiền':<8} | {'Greedy (Tờ)':<12} | {'DP (Tờ)':<12} | {'Time Greedy (ms)':<17} | {'Time DP (ms)':<15} | "
    print(header)
    print("-" * len(header))
    
    # Duyệt và in kết quả từ hàm so sánh
    for case in test_cases:
        print(compare_performance(case))
        
    print("-" * len(header))

if __name__ == "__main__":
    main()