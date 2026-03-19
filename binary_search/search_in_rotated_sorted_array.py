"""
Given a rotated sorted integer array nums and a
target, return the index of target, or -1.

Example:
  Input:  nums=[4,5,6,7,0,1,2], target=0
  Output: 4

Constraints:
  Determine which sorted half mid falls in, then narrow.
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid

            # Check if mid is in the left sorted portion.
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            # Mid is in the right sorted portion.
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
