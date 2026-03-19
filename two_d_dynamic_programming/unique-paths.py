"""
Given an m x n grid, count unique paths from
the top-left to the bottom-right corner. You
may only move right or down.

Example:
  Input:  m=3, n=7
  Output: 28

Constraints:
  Memoized DFS counts paths by branching right
  and down; only the bottom-right cell returns 1.
"""

from functools import cache


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Count leaves (valid endpoints) in the tree.
        @cache
        def dfs(i, j):
            if (i, j) == (m - 1, n - 1):
                return 1
            if i >= m or j >= n:
                return 0
            # Move down or move right.
            return dfs(i + 1, j) + dfs(i, j + 1)

        return dfs(0, 0)
