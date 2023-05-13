"""
strategy to solve the problem:
    problem: given a matrix with 1 is land and 0 is water. island is connected land. compute the largest land insland
    why
        using dfs for explore graph problem
        dfs(r, c):
            base case, return 0 if r, c is not value or (r, c) in visited or is water
            normal case. update visited, count 1 and continue explore 
"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        visited = set()
        h, w = len(grid), len(grid[0])
        area = 0
        def dfs(r, c):
            """
            for each cell visited count as 1
            """
            #base case to stope search
            if (
                r >= h
                or r < 0
                or c >= w
                or c < 0
                or grid[r][c] == 0
                or (r, c) in visited
            ):
                return 0
            #makr visted
            visited.add((r, c))
            #count as 1 and move to children problem
            return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c -1)
        
        for r in range(h):
            for c in range(w):
                #do not repeat calculation with visted cell
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = max(area, dfs(r, c))
        return area