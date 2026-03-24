"""
Problem: Product of Array Except Self

Given an integer array nums, return an array
where answer[i] is the product of all elements
except nums[i]. Do NOT use division.

Example:
  Input:  nums=[1,2,3,4]
  Output: [24,12,8,6]

Approach: Prefix and Postfix Multiplication
  - First pass: Compute running prefix products
    into the result array.
  - Second pass: Compute running postfix products
    and multiply them with the stored prefixes.
"""

from typing import List


class Solution:
    def productExceptSelf(
        self, nums: List[int]
    ) -> List[int]:
        
        res = [1] * len(nums)

        # 1. Forward pass for prefixes
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        # 2. Backward pass for postfixes
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
            
        return res
