"""
Given a list of coin denominations and an amount,
return the number of combinations that make up the
amount. Each coin may be used unlimited times.

Example:
  Input:  amount=5, coins=[1,2,5]
  Output: 4

Constraints:
  DFS: at each coin either take it again or move to next coin.
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
            # Branch 1: take coins[idx] again (unlimited use).
            # Branch 2: skip to the next coin denomination.
            return (
                dfs(idx, total + coins[idx])
                + dfs(idx + 1, total)
            )

        return dfs(0, 0)
