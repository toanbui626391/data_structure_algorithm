"""
Given an array of distinct integers candidates and
a target integer, return all unique combinations
where the chosen numbers sum to target. The same
number may be chosen unlimited times.

Example:
  Input:  candidates=[2,3,6,7], target=7
  Output: [[2,2,3],[7]]

Constraints:
  DFS with index prevents going backward (avoids permutations).
"""

from typing import List


class Solution:
    def combinationSum(
        self, candidates: List[int], target: int
    ) -> List[List[int]]:
        result = []

        def dfs(idx, current, total):
            # Found a valid combination.
            if total == target:
                result.append(current.copy())
                return
            # Exceeded target or exhausted candidates.
            if idx >= len(candidates) or total > target:
                return
            # Branch 1: include candidates[idx] again.
            current.append(candidates[idx])
            dfs(idx, current, total + candidates[idx])
            # Branch 2: skip to the next candidate.
            current.pop()
            dfs(idx + 1, current, total)

        dfs(0, [], 0)
        return result
