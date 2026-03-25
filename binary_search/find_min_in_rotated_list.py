"""
Problem: Find Minimum in Rotated Sorted Array

Given a rotated sorted array nums (no duplicates),
return the minimum element in O(log n) time.

Example:
  Input:  nums=[3,4,5,1,2]
  Output: 1

Approach: Binary Search Boundaries
  - Compare mid with the rightmost element to 
    determine which half spans the pivot (the drop).
  - If mid > right, the pivot is to the right.
  - If mid < right, the right half is sorted,
    so the pivot (min) must be mid or to its left.
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        # We want to narrow the window until left
        # and right converge on the minimum value.
        while left < right:
            mid = left + (right - left) // 2
            
            # Mid is strictly greater than the right 
            # edge. This means the drop (minimum) is
            # somewhere to the right of mid.
            if nums[mid] > nums[right]:
                left = mid + 1
                
            # Mid is less than or equal to the right
            # edge. This means the right side is fully
            # sorted, so the minimum is at mid or left.
            else:
                right = mid
                
        return nums[left]
