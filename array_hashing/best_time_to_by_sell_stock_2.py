def maxProfit(prices: list[int]) -> int:
    total_profit = 0
    
    # Start on day 1 (the second day) so we can compare it to day 0
    for i in range(1, len(prices)):
        
        # If today's price is higher than yesterday's, we "transact"
        if prices[i] > prices[i - 1]:
            # Add the difference to our total profit
            total_profit += prices[i] - prices[i - 1]
            
    return total_profit