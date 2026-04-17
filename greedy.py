def coin_change_greedy(coins, amount):
    """
    coins: danh sách mệnh giá tiền
    amount: số tiền cần đổi
    """
    # Tham lam cần duyệt từ mệnh giá lớn nhất đến nhỏ nhất
    sorted_coins = sorted(coins, reverse=True)
    coins = [c for c in coins if c > 0]
    result = []
    total_coins = 0
    remaining = amount
    
    for coin in sorted_coins:
        # số lượng 'coin' có thể lấy ra 
        count = remaining // coin
        if count > 0:
            result.extend([coin] * count)
            total_coins += count
            remaining %= coin
            
    # nếu còn dư thì không thể đổi chính xác
    if remaining > 0:
        return None, []
        
    return total_coins, result