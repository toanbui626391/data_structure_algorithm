"""
Given a list of coin denominations and an amount,
return the minimum number of coins needed to make
up the amount. Return -1 if impossible.

Example:
  Input:  coins=[1,5,11], amount=15
  Output: 3

Constraints:
  dp[a] = min(dp[a], dp[a-c] + 1) for each coin c.
"""

from typing import List


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # Initialize the dp array with infinity
        # We use amount + 1 as a safe "infinity" because the max possible 
        # coins needed would be 'amount' (using all 1-cent coins)
        dp = [amount + 1] * (amount + 1)
        
        # Base case: 0 coins needed to make amount 0
        dp[0] = 0
        
        # Iterate through all amounts from 1 to the target
        for a in range(1, amount + 1):
            for c in coins:
                # If the coin is smaller or equal to the current amount
                if a - c >= 0:
                    # The core DP formula
                    dp[a] = min(dp[a], dp[a - c] + 1)
                    
        # If the target amount is still "infinity", it means it's impossible
        return dp[amount] if dp[amount] != amount + 1 else -1
