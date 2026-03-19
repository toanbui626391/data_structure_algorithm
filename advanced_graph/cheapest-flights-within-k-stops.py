"""
Given n cities, flights as (u, v, cost) tuples, a
source src, destination dst, and at most k stops,
find the cheapest price. Return -1 if impossible.

Example:
  Input:  n=4, flights=[[0,1,100],[1,2,100],[2,0,100],
          [1,3,600],[2,3,200]], src=0, dst=3, k=1
  Output: 700

Constraints:
  Modified Dijkstra tracking steps prevents exceeding k stops.
"""

from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def findCheapestPrice(
        self, n, flights, src, dst, k
    ):
        # Build adjacency list: node -> list of (neighbor, cost).
        graph = defaultdict(list)
        for origin, dest, cost in flights:
            graph[origin].append((dest, cost))

        # cache tracks minimum cost seen to reach each node.
        cache = [float('inf')] * n
        # Priority queue: (steps_used, node, cumulative_cost).
        priority_queue = []
        heappush(priority_queue, (0, src, 0))

        while priority_queue:
            steps, node, cumulative_cost = heappop(priority_queue)
            # Only expand if within k stops and neighbors exist.
            if steps <= k and node in graph:
                for neighbor, weight in graph[node]:
                    new_cost = weight + cumulative_cost
                    if new_cost < cache[neighbor]:
                        cache[neighbor] = new_cost
                        heappush(
                            priority_queue,
                            (steps + 1, neighbor, new_cost),
                        )
        return cache[dst] if cache[dst] != float('inf') else -1
