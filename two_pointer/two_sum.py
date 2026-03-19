"""
Given an array of integers nums and an integer
target, return indices of the two numbers such
that they add up to target.
Exactly one solution exists; each element used once.

Example:
  Input:  nums=[2,7,11,15], target=9
  Output: [0,1]
"""

from typing import List


class Solution:
    def twoSum(
        self, nums: List[int], target: int
    ) -> List[int]:
        # Map seen values to their index for O(1) lookup.
        keeper = {}
        for i, value in enumerate(nums):
            needed = target - value
            if needed in keeper:
                return [i, keeper[needed]]
            # Record this value so future elements can find it.
            keeper[value] = i
