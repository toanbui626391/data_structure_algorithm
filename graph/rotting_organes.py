"""
In a grid where 0=empty, 1=fresh orange, 2=rotten
orange, every minute a rotten orange rots adjacent
fresh ones. Return minutes until all oranges are
rotten, or -1 if impossible.

Example:
  Input:  grid=[[2,1,1],[1,1,0],[0,1,1]]
  Output: 4

Constraints:
  BFS from all rotten oranges simultaneously gives minimum time.
"""

import collections
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque()
        fresh = 0
        time = 0

        # Seed BFS with all initial rotten oranges.
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r, c))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # Continue while fresh oranges and rotten ones remain.
        while fresh > 0 and queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for delta_r, delta_c in directions:
                    row = r + delta_r
                    col = c + delta_c
                    # Rot an adjacent fresh orange and enqueue it.
                    if (
                        row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        queue.append((row, col))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1
