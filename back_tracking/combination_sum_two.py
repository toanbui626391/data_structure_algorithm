"""
Given candidates (may contain duplicates) and a
target, find all unique combinations that sum to
target. Each number may only be used once.

Example:
  Input:  candidates=[10,1,2,7,6,1,5], target=8
  Output: [[1,1,6],[1,2,5],[1,7],[2,6]]

Constraints:
  Sort first; skip duplicate siblings to avoid duplicate combos.
"""

from typing import List


class Solution:
    def combinationSum2(
        self, candidates: List[int], target: int
    ) -> List[List[int]]:
        result = []
        combination = []
        # Sorting groups duplicates together for easy skipping.
        candidates.sort()

        def dfs(idx, combination, total):
            if total == target:
                result.append(combination[:])
                return
            if total > target or idx > len(candidates):
                return

            prev = None
            for pos in range(idx, len(candidates)):
                # Skip duplicate values at the same depth level.
                if candidates[pos] == prev:
                    continue
                combination.append(candidates[pos])
                dfs(pos + 1, combination, total + candidates[pos])
                prev = candidates[pos]
                combination.pop()

        dfs(0, combination, 0)
        return result
