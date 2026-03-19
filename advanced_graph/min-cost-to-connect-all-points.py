"""
Given a list of points on a 2D plane, find the
minimum cost to connect all points. The cost of
connecting two points is their Manhattan distance.

Example:
  Input:  points=[[0,0],[2,2],[3,10],[5,2],[7,0]]
  Output: 20

Constraints:
  Prim's algorithm with a min-heap builds the MST greedily.
"""

import heapq
from typing import List


class Solution:
    def minCostConnectPoints(
        self, points: List[List[int]]
    ) -> int:
        num_points = len(points)
        min_cost = 0
        visited = [False] * num_points
        # Heap entry: (cost_to_reach, vertex_index).
        priority_queue = [(0, 0)]
        # cost_cache tracks the cheapest edge seen to each vertex.
        cost_cache = {0: 0}

        while priority_queue:
            cost, node = heapq.heappop(priority_queue)

            if visited[node]:
                continue

            visited[node] = True
            min_cost += cost

            # Relax edges to all unvisited vertices.
            for neighbor in range(num_points):
                if not visited[neighbor]:
                    dist = (
                        abs(points[node][0] - points[neighbor][0])
                        + abs(points[node][1] - points[neighbor][1])
                    )
                    if dist < cost_cache.get(neighbor, float('inf')):
                        cost_cache[neighbor] = dist
                        heapq.heappush(
                            priority_queue, (dist, neighbor)
                        )

        return min_cost
