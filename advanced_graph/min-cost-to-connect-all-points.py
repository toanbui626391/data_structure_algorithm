import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        min_cost = 0
        #check nodes have been visited
        visited = [False] * n
        #keep track of min cost and vertex
        pq = [(0, 0)]  # (cost, vertex)
        
        cache = {0: 0} #{v: cost}

        while pq:
            cost, u = heapq.heappop(pq)

            if visited[u]:
                continue

            visited[u] = True
            min_cost += cost
            #traverse through vertex by layer
            for v in range(n):
                if not visited[v]:
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    if dist < cache.get(v, float('inf')):
                        cache[v] = dist
                        heapq.heappush(pq, (dist, v))

        return min_cost        