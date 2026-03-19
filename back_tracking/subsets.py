"""
Given an integer array nums of unique elements,
return all possible subsets (the power set).

Example:
  Input:  nums=[1,2,3]
  Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Constraints:
  Each element has exactly two choices: include or exclude.
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(idx):
            # Reached the end; record this subset.
            if idx >= len(nums):
                result.append(values[:])
                return
            # Branch 1: include nums[idx].
            values.append(nums[idx])
            dfs(idx + 1)
            # Branch 2: exclude nums[idx].
            values.pop()
            dfs(idx + 1)

        result = []
        values = []
        dfs(0)
        return result
