"""
Given an unsorted array of integers nums, return
the length of the longest consecutive elements
sequence.

Example:
  Input:  nums=[100,4,200,1,3,2]
  Output: 4  (sequence: 1,2,3,4)

Constraints:
  Must run in O(n) time.
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # A set reduces membership checks to O(1).
        set_nums = set(nums)
        longest = 0
        length = 0
        for element in set_nums:
            # Only start counting from the head of a sequence.
            if element - 1 not in set_nums:
                length = 1
                while element + length in set_nums:
                    length += 1
            longest = max(length, longest)
        return longest
