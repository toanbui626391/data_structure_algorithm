"""
strategy to solve the problem
    problem:
        given a list of point (x,y) find the kth closed point to the origin
    why:
        using min heap because it will pop the smallest element. Therefore we pop kth we will have kth smallest element
        formular to compute distance between two spoint: sqr((x2-x1)^2 + (y2-y1)^2)
"""
import heapq
from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [[x**2 + y**2, x, y] for x, y in points]
        heapq.heapify(distances)
        res = []
        while k > 0:
            temp  = heapq.heappop(distances)
            res.append([temp[1], temp[2]])
            k -= 1
        return res