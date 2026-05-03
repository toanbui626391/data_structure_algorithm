"""
Problem:
Given prices, find max profit with at most one
share held at a time. After selling you must
wait one day (cooldown) before buying again.

Examples:
Input: prices = [1, 2, 3, 0, 2]
Output: 3

Constraints:
1 <= prices.length <= 5000
0 <= prices[i] <= 1000
"""

from typing import List
from functools import cache


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dfs(idx, buying):
            # No profit possible past the end.
            if idx >= len(prices):
                return 0
                
            # Option 1: do nothing (skip).
            profit_cool = dfs(idx + 1, buying)
            
            if buying:
                # Option 2: buy at current price.
                profit_buy = dfs(idx + 1, False) - prices[idx]
                return max(profit_cool, profit_buy)
            else:
                # Option 2: sell and skip day for cooldown.
                profit_sell = dfs(idx + 2, True) + prices[idx]
                return max(profit_cool, profit_sell)

        return dfs(0, True)

def maxProfit(prices):
    if not prices:
        return 0
    
    # Initial states for Day 0
    # We use -float('inf') for hold because we haven't bought anything yet
    hold = -prices[0] 
    sell = 0
    rest = 0
    
    for i in range(1, len(prices)):
        prev_hold = hold
        prev_sell = sell
        prev_rest = rest
        
        # Transitions
        hold = max(prev_hold, prev_rest - prices[i])
        sell = prev_hold + prices[i]
        rest = max(prev_rest, prev_sell)
        
    # The answer is the max of being in the Sold or Rest state on the last day.
    # (You wouldn't want to end the period still holding a stock!)
    return max(sell, rest)


if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1
    prices_1 = [1, 2, 3, 0, 2]
    res_dfs_1 = sol.maxProfit(prices_1)
    res_dp_1 = maxProfit(prices_1)
    
    print("Test 1:")
    print(f"Input: {prices_1}")
    print(f"DFS output: {res_dfs_1}")
    print(f"DP output:  {res_dp_1}")
    print()
    
    # Test case 2
    prices_2 = [1]
    res_dfs_2 = sol.maxProfit(prices_2)
    res_dp_2 = maxProfit(prices_2)
    
    print("Test 2:")
    print(f"Input: {prices_2}")
    print(f"DFS output: {res_dfs_2}")
    print(f"DP output:  {res_dp_2}")
