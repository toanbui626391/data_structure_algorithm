"""
Given an integer array nums, find the subarray with
the largest product and return that product.

Example:
  Input:  nums=[2,3,-2,4]
  Output: 6

Constraints:
  Track both curMin and curMax because a negative times negative
  can flip the min to the max.
"""

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Both start at 1 so the first element sets the value.
        cur_min = 1
        cur_max = 1
        result = nums[0]
        for value in nums:
            candidates = (value, value * cur_min, value * cur_max)
            cur_min = min(candidates)
            cur_max = max(candidates)
            result = max(result, cur_max)
        return result
