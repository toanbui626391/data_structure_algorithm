"""
Given an array of balloon values, burst all
balloons to maximize coins. Bursting balloon i
earns nums[i-1] * nums[i] * nums[i+1] coins.

Example:
  Input:  nums=[3,1,5,8]
  Output: 167

Constraints:
  Interval DP: choose the last balloon to burst
  in each subrange to avoid dependency issues.
"""

from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Pad with sentinel balloons of value 1.
        nums = [1] + nums + [1]
        memo = {}

        def dfs(left, right):
            if left > right:
                return 0
            if (left, right) in memo:
                return memo[(left, right)]

            memo[(left, right)] = 0
            for i in range(left, right + 1):
                # Treat i as the last balloon burst.
                coins = (
                    nums[left - 1]
                    * nums[i]
                    * nums[right + 1]
                )
                coins += (
                    dfs(left, i - 1)
                    + dfs(i + 1, right)
                )
                memo[(left, right)] = max(
                    memo[(left, right)], coins
                )

            return memo[(left, right)]

        return dfs(1, len(nums) - 2)
