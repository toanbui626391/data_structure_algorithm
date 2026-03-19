"""
Given a heights grid where water flows to adjacent
cells with equal or lower height, find all cells
from which water can flow to both the Pacific Ocean
(top/left border) and the Atlantic Ocean (bottom/right).

Example:
  Input:  heights=[[1,2,2,3,5],[3,2,3,4,4],...]
  Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

Constraints:
  Reverse DFS from ocean borders finds all reachable cells.
"""

from typing import List


class Solution:
    def pacificAtlantic(
        self, heights: List[List[int]]
    ) -> List[List[int]]:
        num_rows = len(heights)
        num_cols = len(heights[0])

        def dfs(r, c, visited, prev_height):
            """
            Mark cells reachable by flowing uphill from an ocean.
            """
            if (
                r >= num_rows
                or r < 0
                or c >= num_cols
                or c < 0
                or heights[r][c] < prev_height
                or (r, c) in visited
            ):
                return
            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        pacific = set()
        atlantic = set()

        for r in range(num_rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, num_cols - 1, atlantic, heights[r][num_cols - 1])
        for c in range(num_cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(num_rows - 1, c, atlantic, heights[num_rows - 1][c])

        # Collect cells reachable from both oceans.
        result = []
        for r in range(num_rows):
            for c in range(num_cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append((r, c))
        return result
