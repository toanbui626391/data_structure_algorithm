"""
strategy to solve the problem
    problem: 
        given heights grid each cell is heigh of land
        we have pacific ocean from top and left. atlantic ocean from bottom and right
        return a list of cell (r, c) which water can flow to both pacific and atlantic
    why:
        using dfs(r, c, visited, prevHeight) for exploration and return a set of cell which water can flow. we will star search from pacific and atlantic
"""
from typing import List
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        h, w = len(heights), len(heights[0])

        def dfs(r, c, visited, prevHeight):
            """
            r, c (int): index position of the current cell
            visisted (set): set of cell have been visited so far
            preHeight (int): height of the previous cell
            return set of cell which water can flow to pacific or atlantic
            """
            #base case
            if (
                r >= h
                or r < 0
                or c >= w
                or c < 0
                or heights[r][c] < prevHeight
                or (r, c) in visited
            ):
                return
            visited.add((r, c))
            #explore neighbors cell
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])

        #collect cell from pacific and atl
        pac, atl = set(), set()
        for r in range(h):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, w-1, atl, heights[r][w-1])
        for c in range(w):
            dfs(0, c, pac, heights[0][c])
            dfs(h-1, c, atl, heights[h-1][c])
        
        #collect cel from atlantic
        res = []
        for r in range(h):
            for c in range(w):
                if (r, c) in pac and (r, c) in atl:
                    res.append((r,c))
        return res