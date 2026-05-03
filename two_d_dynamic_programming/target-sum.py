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

    def findTargetSumWaysDP(nums, target):
        total_sum = sum(nums)
        
        # Check if the target is physically possible
        if abs(target) > total_sum or (target + total_sum) % 2 != 0:
            return 0
        
        # Calculate our new subset target 'S'
        subset_target = (target + total_sum) // 2
        
        # This is now exactly like "Coin Change 2" but with one-time use items
        dp = [0] * (subset_target + 1)
        dp[0] = 1 # Base case: one way to make sum 0
        
        for num in nums:
            # Iterate backwards to ensure each number is used only once
            for i in range(subset_target, num - 1, -1):
                dp[i] += dp[i - num]
                
        return dp[subset_target]        
