"""
strategy to solve the problem
    problem: you have a list of stones. You pick the two largest and smash it together. if equal both of them are disappear if not larger - smaller is the remain and put back to stone list.
        do this until the last stones remain
"""
from typing import List
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #using max heap
        stones = [-s for s in stones]
        heapq.heapify(stones)
        first = heapq.heappop(stones)
        second = heapq.heappop(stones)
        while len(stones) > 1:
            if first < second: #remember we in reverse order
                heapq.heappush(stones, first - second)
        stones.append(0) #for case of empty stones
        return abs(stones[0])