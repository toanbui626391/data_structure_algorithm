"""
Given an integer array nums, return true if you can
partition it into two subsets with equal sum.

Example:
  Input:  nums=[1,5,11,5]
  Output: True  ([1,5,5] and [11])

Constraints:
  If total is odd, equal partition is impossible.
  This is a 0/1 knapsack problem targeting total/2.
"""

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        # An odd total cannot be split into two equal halves.
        if total & 1:
            return False
        half = total >> 1
        # dp[curr] means a subset summing to curr is achievable.
        dp = [True] + [False] * half
        for num in nums:
            # Iterate in reverse to avoid using num more than once.
            for curr in range(half, num - 1, -1):
                dp[curr] = dp[curr] or dp[curr - num]
        return dp[-1]
