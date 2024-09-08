from heapq import heappop, heappush
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        n = len(grid)

        pq = [(grid[0][0], 0, 0)] #(time, r, c)
        visited = set() #v
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited.add((0, 0))
        while pq:
            min_time, r, c = heappop(pq)
            # visited.add((r, c))

            if r == n-1 and c == n-1:
                return min_time
            #move to neighbors
            for dx, dy in directions:
                r_dx, c_dy = r + dx, c + dy
                if 0 <= r_dx < n and 0 <= c_dy < n and (r_dx, c_dy) not in visited:
                    heappush(pq, (max(grid[r_dx][c_dy], min_time), r_dx, c_dy))
                    visited.add((r_dx, c_dy))
        
            