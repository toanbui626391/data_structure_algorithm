"""
Given an m x n matrix, return the length of
the longest strictly increasing path. You may
move in four directions (no diagonals).

Example:
  Input:  matrix=[[9,9,4],[6,6,8],[2,1,1]]
  Output: 4

Constraints:
  DFS with memoization; each cell's result only
  depends on neighbors with strictly greater
  values, so no visited set is needed.
"""

from typing import List


class Solution:
    def longestIncreasingPath(
        self, matrix: List[List[int]]
    ) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        memo = {}

        def dfs(r, c, prev_val):
            if (
                r < 0
                or r == ROWS
                or c < 0
                or c == COLS
                or matrix[r][c] <= prev_val
            ):
                return 0
            if (r, c) in memo:
                return memo[(r, c)]

            current_val = matrix[r][c]
            best = 1
            best = max(
                best, 1 + dfs(r + 1, c, current_val)
            )
            best = max(
                best, 1 + dfs(r - 1, c, current_val)
            )
            best = max(
                best, 1 + dfs(r, c + 1, current_val)
            )
            best = max(
                best, 1 + dfs(r, c - 1, current_val)
            )
            memo[(r, c)] = best
            return best

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)
        return max(memo.values())
