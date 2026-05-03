"""
Problem:
Given a list of coin denominations and an amount,
return the number of combinations that make up the
amount. Each coin may be used unlimited times.

Examples:
Input: amount = 5, coins = [1, 2, 5]
Output: 4

Constraints:
1 <= coins.length <= 300
1 <= coins[i] <= 5000
0 <= amount <= 5000
"""

from typing import List
from functools import cache


class Solution:
    def change(
        self, amount: int, coins: List[int]
    ) -> int:
        @cache
        def dfs(idx, total):
            if total == amount:
                return 1
            
            if total > amount:
                return 0
            
            if idx >= len(coins):
                return 0
            
            # Branch 1: take coin again (unlimited use).
            take_coin = dfs(idx, total + coins[idx])
            
            # Branch 2: skip to the next coin.
            skip_coin = dfs(idx + 1, total)
            
            return take_coin + skip_coin

        return dfs(0, 0)

    def changeDP(
        self, amount: int, coins: List[int]
    ) -> int:
        # dp[i] tracks the number of combinations
        # to make up the amount i.
        dp = [0] * (amount + 1)
        
        # Base case: 1 way to make amount 0.
        dp[0] = 1
        
        # Loop through coins first to find combinations,
        # rather than permutations.
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = dp[i] + dp[i - coin]
                
        return dp[amount]


if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1
    amount_1 = 5
    coins_1 = [1, 2, 5]
    
    res_dfs_1 = sol.change(amount_1, coins_1)
    res_dp_1 = sol.changeDP(amount_1, coins_1)
    
    print("Test 1:")
    print(f"Input: amount={amount_1}, coins={coins_1}")
    print(f"DFS output: {res_dfs_1}")
    print(f"DP output:  {res_dp_1}")
    print()
    
    # Test case 2
    amount_2 = 3
    coins_2 = [2]
    
    res_dfs_2 = sol.change(amount_2, coins_2)
    res_dp_2 = sol.changeDP(amount_2, coins_2)
    
    print("Test 2:")
    print(f"Input: amount={amount_2}, coins={coins_2}")
    print(f"DFS output: {res_dfs_2}")
    print(f"DP output:  {res_dp_2}")
