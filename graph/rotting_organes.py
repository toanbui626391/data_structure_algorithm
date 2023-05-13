"""
strate gy to solve the problem
    problem:
        given a grid of cells which have one of three values (0: empty cell, 1: fresh , 2: rotten)
    why:
        using bfs because we have to count and check does fresh organ exist
        bfs:
            outter while loop to check for condition to stop searching
            bfs using que and layer to store job to process
                process by layer each layer to find number of job to process that layer
                for each job have been process add back to que for next exploring that step
"""
import collections
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh = 0 #to hold the current rotten organ and prepare for next time process
        time = 0
        #init fresh and rotten organe in que
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        #still have fresh organe and still have que to process
        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft() #process depth of the tree first
                #from current rotten, make jacent fresh cell rotten, and append to que for next process
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    #check for valid condition (and) to turn fresh to rotten
                    if (
                        row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1
