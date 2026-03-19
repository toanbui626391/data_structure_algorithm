"""
Given an m x n 2D binary grid where '1' is land
and '0' is water, return the number of islands.
An island is surrounded by water and formed by
connecting adjacent lands horizontally or vertically.

Example:
  Input:  grid=[["1","1","0","0","0"],["1","1","0","0","0"],
          ["0","0","1","0","0"],["0","0","0","1","1"]]
  Output: 3

Constraints:
  DFS from each unvisited land cell marks an entire island.
"""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        islands = 0
        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            # Stop at boundaries, water, or already-visited cells.
            if (
                r not in range(rows)
                or c not in range(cols)
                or grid[r][c] == "0"
                or (r, c) in visited
            ):
                return

            visited.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for delta_r, delta_c in directions:
                dfs(r + delta_r, c + delta_c)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    dfs(r, c)
        return islands
