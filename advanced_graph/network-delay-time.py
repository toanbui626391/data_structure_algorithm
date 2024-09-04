from collections import defaultdict
from heapq import heappop, heappush
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:        

        #dijkstra's algo
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((w, v))
        
        pq = [(0, k)]
        visited = set()

        while pq:
            travel_time, u = heappop(pq)

            visited.add(u)
            if len(visited) == n:
                return travel_time

            for (w, v) in graph[u]:
                if v not in visited:
                    #carry travel_time
                    heappush(pq, (travel_time+w, v))
        return -1
