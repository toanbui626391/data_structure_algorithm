"""
strategy to solve the problem
    problem: 
        given a grid of wall (1), gate (0) and romm(INF). find the smallest distance between room and gate
    why:
        #using bfs() to compute distance between gate and room all as the game time and choose min distance
"""
from typing import List
from collections import deque
class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """

    def walls_and_gates(self, rooms: List[List[int]]):
        ROWS, COLS = len(rooms), len(rooms[0])
        visit = set()
        q = deque() #que task for bfs

        def addRooms(r, c):
            """
            heper function for bfs() which will stope add invalida move and update visit and que
            """
            if (
                min(r, c) < 0
                or r == ROWS
                or c == COLS
                or (r, c) in visit #prevent larger distance to assigned to cell
                or rooms[r][c] == -1#stop when meet wall
            ):
                return
            visit.add((r, c))
            q.append([r, c])

        #init que and visit with gate cells
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))
        #string bfs
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = dist
                addRooms(r + 1, c)
                addRooms(r - 1, c)
                addRooms(r, c + 1)
                addRooms(r, c - 1)
            dist += 1
