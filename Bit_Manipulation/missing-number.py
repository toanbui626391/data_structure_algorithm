"""
Given an array of n distinct numbers in [0, n],
return the one missing number.

Example:
  Input:  nums=[3,0,1]
  Output: 2

Constraints:
  XOR every index 1..n with every element;
  duplicate values cancel, leaving the missing one.
"""

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # XOR properties: x^x=0, x^0=x, commutative.
        count = len(nums)
        result = 0
        for i in range(1, count + 1):
            result ^= i
        for num in nums:
            result ^= num
        return result
