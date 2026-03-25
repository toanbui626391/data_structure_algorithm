"""
Problem: Search in Rotated Sorted Array

Given a rotated sorted integer array nums and a
target, return the index of target, or -1.

Example:
  Input:  nums=[4,5,6,7,0,1,2], target=0
  Output: 4

Approach: Binary Search
  - Since the array is rotated, one half of the
    array (from mid) will always be strictly sorted.
  - Find out which half is sorted.
  - Check if the target falls strictly within the
    sorted half's boundaries to decide which half
    to discard.
"""

from typing import List


class Solution:
    def search(
        self, nums: List[int], target: int
    ) -> int:
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid

            # Check if left portion is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
                    
            # Otherwise, the right portion is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return -1
