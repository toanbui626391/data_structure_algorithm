"""
Given an integer array nums that may contain
duplicates, return all possible unique subsets.

Example:
  Input:  nums=[1,2,2]
  Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Constraints:
  Sort first; when skipping an element, skip all its duplicates.
"""

from typing import List


class Solution:
    def subsetsWithDup(
        self, nums: List[int]
    ) -> List[List[int]]:
        result = []
        # Sorting groups duplicates so we can skip them.
        nums.sort()

        def backtrack(idx, subset):
            if idx == len(nums):
                result.append(subset[::])
                return

            # Branch 1: include nums[idx].
            subset.append(nums[idx])
            backtrack(idx + 1, subset)
            subset.pop()

            # Branch 2: exclude nums[idx] and all its duplicates.
            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1
            backtrack(idx + 1, subset)

        backtrack(0, [])
        return result
