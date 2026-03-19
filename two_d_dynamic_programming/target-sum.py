"""
Given an integer array nums and an integer target,
assign '+' or '-' to each number and return the
number of ways to reach the target sum.

Example:
  Input:  nums=[1,1,1,1,1], target=3
  Output: 5

Constraints:
  DFS with memoization covers all +/- assignment combinations.
"""

from typing import List
from functools import cache


class Solution:
    def findTargetSumWays(
        self, nums: List[int], target: int
    ) -> int:
        @cache
        def dfs(idx, total):
            # Finished assigning all numbers; check target.
            if idx >= len(nums):
                return 1 if total == target else 0
            # Try adding and subtracting the current number.
            return (
                dfs(idx + 1, total + nums[idx])
                + dfs(idx + 1, total - nums[idx])
            )

        return dfs(0, 0)
