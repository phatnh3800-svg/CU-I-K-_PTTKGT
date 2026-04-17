import time
from dynamic_programming import coin_change_dp
from greedy import coin_change_greedy

def compare_performance(case):
    coins, amount = case["coins"], case["amount"]
    
    # 1. Đo lường Greedy
    start_g = time.perf_counter()
    count_g, _ = coin_change_greedy(coins, amount)
    time_g = (time.perf_counter() - start_g) * 1000
    
    # 2. Đo lường DP
    start_dp = time.perf_counter()
    count_dp, _ = coin_change_dp(coins, amount)
    time_dp = (time.perf_counter() - start_dp) * 1000
    
    # 3. Xử lý logic trạng thái
    str_g = str(count_g) if count_g is not None else "N/A"
    str_dp = str(count_dp) if count_dp is not None else "N/A"
        
    coins_str = ", ".join(map(str, case['coins']))
    return f" {case['id']:<3} | {case['name']:<25} | {coins_str:<40} | {amount:<8} | {str_g:<12} | {str_dp:<12} | {time_g:<17.4f} | {time_dp:<15.4f} |"