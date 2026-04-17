from compare_performance import compare_performance
def main(): 
    while True:
        try:
            raw_coins = input("Nhập các mệnh giá tiền (cách nhau bởi dấu phẩy): ")
            coins = [int(c.strip()) for c in raw_coins.split(",")]
            
            amount = int(input("Nhập số tiền cần đổi: "))
            
            manual_case = {
                "id": 1,
                "name": "Nhập từ bàn phím",
                "coins": coins,
                "amount": amount
            }
            
            header = f" {'ID':<3} | {'Tên':<25} | {'Mệnh giá':<40} | {'Tiền':<8} | {'Greedy (Tờ)':<12} | {'DP (Tờ)':<12} |{'Time Greedy (ms)':<17} | {'Time DP (ms)':<15} |"
            print("\n" + header)
            print("-" * len(header))
            
            print(compare_performance(manual_case))
            print("-" * len(header))

        except ValueError:
            print("\nLỗi đầu vào")
        except Exception as e:
            print(f"\nLỗi {e}")

        cont = input("\nBạn có muốn tiếp tục không? (y/n): ").strip().lower()
        if cont != 'y':
            print("Cảm ơn bạn đã sử dụng chương trình. Tạm biệt!")
            break

if __name__ == "__main__":
    main()