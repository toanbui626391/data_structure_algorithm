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
  def lengthOfLIS(nums):
      if not nums: return 0
      
      # Every element is a subsequence of length 1
      dp = [1] * len(nums)
      
      for i in range(len(nums)):
          for j in range(i):
              if nums[j] < nums[i]:
                  dp[i] = max(dp[i], dp[j] + 1)
                  
      return max(dp)
