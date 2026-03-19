"""
Given an integer array nums, return an array
answer such that answer[i] is equal to the
product of all elements of nums except nums[i].

Must run in O(n) time without division.

Example:
  Input:  nums=[1,2,3,4]
  Output: [24,12,8,6]
"""

from typing import List


class Solution:
    def productExceptSelf(
        self, nums: List[int]
    ) -> List[int]:
        result = [1] * len(nums)

        # Forward pass fills prefix products.
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        # Backward pass multiplies in postfix products.
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        return result
