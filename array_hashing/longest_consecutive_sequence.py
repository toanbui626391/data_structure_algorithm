"""
Problem: Longest Consecutive Sequence

Given an unsorted array of integers nums, return
the length of the longest consecutive sequence.

Example:
  Input:  nums=[100,4,200,1,3,2]
  Output: 4  (sequence: 1, 2, 3, 4)

Approach: Hash Set
  - Use a set for O(1) membership checks.
  - Only start counting from the 'head' of a 
    sequence (where num - 1 is NOT in the set).
  - This prevents redundant O(N²) work, achieving
    strict O(N) time complexity.
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            # Check if it's the start of a sequence
            if (num - 1) not in num_set:
                length = 1
                
                # Expand the sequence
                while (num + length) in num_set:
                    length += 1
                    
                longest = max(length, longest)
                
        return longest
