"""
Count the number of distinct ways to climb n stairs,
taking 1 or 2 steps at a time.

Example:
  Input:  n=3
  Output: 3  (1+1+1, 1+2, 2+1)

Constraints:
  dp[n] = dp[n-1] + dp[n-2] because each step comes from 1 or 2 below.
"""

from functools import cache


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        # Rolling variables avoid allocating a full dp array.
        current = 1
        previous = 1
        for i in range(2, n + 1):
            current, previous = current + previous, current
        return current
