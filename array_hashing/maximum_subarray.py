"""
Problem: Maximum Subarray

Given an integer array nums, return the subarray
with the largest sum, and return its sum.

Example:
  Input:  nums=[-2,1,-3,4,-1,2,1,-5,4]
  Output: 6  (subarray: [4,-1,2,1])

Approach: Kadane's Algorithm
  - Iterate through the array keeping a running sum.
  - If the running sum becomes negative, it hurts
    future windows. Reset it to 0.
  - Constantly track the max sum seen.
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = nums[0]
        current_sum = 0

        for num in nums:
            # Drop a negative prefix sum
            if current_sum < 0:
                current_sum = 0
                
            current_sum += num
            
            # Update best seen
            if current_sum > best_sum:
                best_sum = current_sum

        return best_sum
