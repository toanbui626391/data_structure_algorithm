"""
Given an integer array nums, return the length of
the longest strictly increasing subsequence.

Example:
  Input:  nums=[10,9,2,5,3,7,101,18]
  Output: 4  ([2,3,7,101])

Constraints:
  dp[i] = max length of increasing subarray ending at index i.
"""

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] starts at 1 (the element alone).
        dp = [1] * len(nums)

        for i in range(len(nums)):
            for pos in range(i):
                if nums[pos] < nums[i]:
                    # Extend any increasing subarray ending at pos.
                    dp[i] = max(dp[i], dp[pos] + 1)
        return max(dp)
