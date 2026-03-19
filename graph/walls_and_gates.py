"""
Given a grid of walls (-1), gates (0), and rooms
(INF), fill each room with its distance to the
nearest gate. Walls cannot be crossed.

Example:
  Input:  rooms=[[INF,-1,0,INF],[INF,INF,INF,-1],
          [INF,-1,INF,-1],[0,-1,INF,INF]]
  Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

Constraints:
  BFS from all gates simultaneously assigns minimum distances.
"""

from typing import List
from collections import deque


class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """

    def walls_and_gates(self, rooms: List[List[int]]):
        ROWS = len(rooms)
        COLS = len(rooms[0])
        visited = set()
        queue = deque()

        def add_room(r, c):
            """
            Add a valid, unvisited non-wall room to the queue.
            """
            if (
                min(r, c) < 0
                or r == ROWS
                or c == COLS
                or (r, c) in visited
                or rooms[r][c] == -1
            ):
                return
            visited.add((r, c))
            queue.append([r, c])

        # Seed BFS from all gate positions simultaneously.
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    queue.append([r, c])
                    visited.add((r, c))

        dist = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                rooms[r][c] = dist
                add_room(r + 1, c)
                add_room(r - 1, c)
                add_room(r, c + 1)
                add_room(r, c - 1)
            dist += 1
