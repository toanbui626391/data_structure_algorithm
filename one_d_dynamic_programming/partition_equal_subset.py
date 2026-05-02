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
  def canPartition(nums):
      total_sum = sum(nums)
      
      # If the sum is odd, we can't split it equally
      if total_sum % 2 != 0:
          return False
      
      target = total_sum // 2
      # dp[i] will be True if a sum of i is possible
      dp = [False] * (target + 1)
      dp[0] = True
      
      for num in nums:
          # Iterate backwards to avoid using the current num multiple times
          for i in range(target, num - 1, -1):
              if dp[i - num]:
                  dp[i] = True
          
          # Optimization: If we found the target, we can stop early
          if dp[target]:
              return True
              
      return dp[target]
