"""
Given a binary matrix where 1 is land and 0 is
water, return the maximum area of an island.

Example:
  Input:  grid=[[0,0,1,0,0,0,0,1,0,0,0,0,0],...]
  Output: 6

Constraints:
  DFS counts cells in one island; take the maximum.
"""

from typing import List


class Solution:
    def maxAreaOfIsland(
        self, grid: List[List[int]]
    ) -> int:
        visited = set()
        num_rows = len(grid)
        num_cols = len(grid[0])
        area = 0

        def dfs(r, c):
            # Return 0 for out-of-bounds, water, or visited cells.
            if (
                r >= num_rows
                or r < 0
                or c >= num_cols
                or c < 0
                or grid[r][c] == 0
                or (r, c) in visited
            ):
                return 0
            visited.add((r, c))
            # Count this cell plus all adjacent land cells.
            return (
                1
                + dfs(r + 1, c)
                + dfs(r - 1, c)
                + dfs(r, c + 1)
                + dfs(r, c - 1)
            )

        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = max(area, dfs(r, c))
        return area
