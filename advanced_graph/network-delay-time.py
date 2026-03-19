"""
Given a network of n nodes, directed edges times as
(u, v, weight), and a starting node k, return how
long it takes for all nodes to receive the signal.
Return -1 if impossible.

Example:
  Input:  times=[[2,1,1],[2,3,1],[3,4,1]], n=4, k=2
  Output: 2

Constraints:
  Dijkstra's algorithm finds shortest paths from the source.
"""

from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def networkDelayTime(
        self,
        times: List[List[int]],
        n: int,
        k: int,
    ) -> int:
        # Build adjacency list: node -> list of (cost, neighbor).
        graph = defaultdict(list)
        for origin, dest, weight in times:
            graph[origin].append((weight, dest))

        # Min-heap: (accumulated_time, node).
        priority_queue = [(0, k)]
        visited = set()

        while priority_queue:
            travel_time, node = heappop(priority_queue)
            visited.add(node)
            # All n nodes reached; travel_time is the max delay.
            if len(visited) == n:
                return travel_time

            for weight, neighbor in graph[node]:
                if neighbor not in visited:
                    heappush(
                        priority_queue,
                        (travel_time + weight, neighbor),
                    )
        return -1
