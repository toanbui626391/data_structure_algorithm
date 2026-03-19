"""
Given an array where every element appears
twice except one, return the single element.

Example:
  Input:  nums=[4,1,2,1,2]
  Output: 4

Constraints:
  XOR all values: duplicate pairs cancel to 0,
  leaving only the unique element.
"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Duplicates XOR to 0; only unique survives.
        result = 0
        for num in nums:
            result ^= num
        return result
