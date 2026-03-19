"""
Given a 1-indexed sorted array numbers, find two
numbers that add up to target. Return their indices.
Each input has exactly one solution.

Example:
  Input:  numbers=[2,7,11,15], target=9
  Output: [1,2]

Constraints:
  The sorted order allows two-pointer convergence.
"""

from typing import List


class Solution:
    def twoSum(
        self, numbers: List[int], target: int
    ) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                # Return 1-indexed positions.
                return [left + 1, right + 1]
            if total > target:
                right -= 1
            if total < target:
                left += 1
