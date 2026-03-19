"""
Given an n x n integer grid where grid[i][j] is the
elevation at (i, j), you can swim from cell to cell
if the current water level >= both cells' elevations.
Find the minimum time to swim from top-left to bottom-right.

Example:
  Input:  grid=[[0,2],[1,3]]
  Output: 3

Constraints:
  Dijkstra minimizes the maximum elevation along the path.
"""

from heapq import heappop, heappush
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)

        # Heap entry: (max_elevation_so_far, row, col).
        priority_queue = [(grid[0][0], 0, 0)]
        visited = set()
        visited.add((0, 0))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while priority_queue:
            min_time, r, c = heappop(priority_queue)

            # Reached the destination.
            if r == num_rows - 1 and c == num_rows - 1:
                return min_time

            for delta_r, delta_c in directions:
                next_r = r + delta_r
                next_c = c + delta_c
                if (
                    0 <= next_r < num_rows
                    and 0 <= next_c < num_rows
                    and (next_r, next_c) not in visited
                ):
                    # Time is the max elevation along the path.
                    heappush(
                        priority_queue,
                        (
                            max(grid[next_r][next_c], min_time),
                            next_r,
                            next_c,
                        ),
                    )
                    visited.add((next_r, next_c))
