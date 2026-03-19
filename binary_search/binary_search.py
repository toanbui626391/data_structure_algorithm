"""
Given a sorted array nums and a target, return the
index of target if found, otherwise return -1.

Example:
  Input:  nums=[-1,0,3,5,9,12], target=9
  Output: 4

Constraints:
  The sorted order allows O(log n) binary search.
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            # Avoid integer overflow compared to (l+r)//2.
            mid = left + ((right - left) // 2)
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1
