#Modified Dijkstra's Algorithm
from collections import defaultdict
from heapq import *
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        #compute min_cost

        #build graph
        graph = defaultdict(list)
        for u,v, cost in flights:
            # graph.setdefault(u,[])
            graph[u].append((v,cost))

        #
        cache, pq = [float('inf')] * n ,[]
        #our source u starts with a value of 0
        heappush(pq,(0,src,0)) #(steps, u, cost)
        
        while pq:
            #on each iteration pop from the queue
            steps,u,cost = heappop(pq)
            #we're only going to add more us to the queue if they've
            #taken less than k+1 steps, and their children are present
            #in the adjacency list
            if steps<=k and u in graph:
                #go through the current us neighbours
                for v,w in graph[u]:
                    #the path to this u is less than the smallest we've
                    #every seen at v
                    #then relax the edge
                    if w + cost < cache[v]:
                        #and set the v to the new value
                        cache[v] = w + cost
                        #add the v to the heap for further processing
                        heappush(pq,(steps+1, v, w+cost))
        return cache[dst] if cache[dst] != float('inf') else -1