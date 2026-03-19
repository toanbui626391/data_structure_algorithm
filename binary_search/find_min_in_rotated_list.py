"""
Given a rotated sorted array nums (no duplicates),
return the minimum element.

Example:
  Input:  nums=[3,4,5,1,2]
  Output: 1

Constraints:
  Elements left of the pivot are all greater than elements
  right of the pivot, enabling binary search.
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        result = nums[-1]
        while left <= right:
            mid = (left + right) // 2
            # Mid is in the higher (left) section of rotation.
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                # Mid is in the lower (right) section.
                right = mid - 1
                result = min(result, nums[mid])
        return result
