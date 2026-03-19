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
    def coinChange(
        self, coins: List[int], amount: int
    ) -> int:
        # dp[a] is the minimum coins to reach amount a.
        dp = [float("inf")] * (amount + 1)
        # Zero coins are needed to make amount 0.
        dp[0] = 0
        for coin in coins:
            for target in range(coin, amount + 1):
                dp[target] = min(
                    dp[target], dp[target - coin] + 1
                )
        return -1 if dp[-1] == float("inf") else dp[-1]
