"""
Given prices, find max profit with at most one share
held at a time. After selling you must wait one day
(cooldown) before buying again.

Example:
  Input:  prices=[1,2,3,0,2]
  Output: 3

Constraints:
  DFS with (index, buying_state) captures all valid transitions.
"""

from typing import List
from functools import cache


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dfs(idx, buying):
            # No profit possible past the end of prices.
            if idx >= len(prices):
                return 0
            # Option 1: do nothing (cooldown/skip).
            profit_cool = dfs(idx + 1, buying)
            if buying:
                # Option 2: buy at current price.
                profit_buy = dfs(idx + 1, not buying) - prices[idx]
                return max(profit_cool, profit_buy)
            else:
                # Option 2: sell and skip one day for cooldown.
                profit_sell = dfs(idx + 2, not buying) + prices[idx]
                return max(profit_cool, profit_sell)

        return dfs(0, True)
