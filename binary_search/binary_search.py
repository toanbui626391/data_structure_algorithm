"""
Problem: Binary Search

Given a sorted array nums and a target, return the
index of target if found, otherwise return -1.

Example:
  Input:  nums=[-1,0,3,5,9,12], target=9
  Output: 4

Approach: Search Space Reduction
  - Array must be sorted.
  - Check the middle element.
  - If equal, return index.
  - If target is smaller, search left half.
  - If target is larger, search right half.
"""

from typing import List


class Solution:
    def search(
        self, nums: List[int], target: int
    ) -> int:
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            # Prevent integer overflow
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1
