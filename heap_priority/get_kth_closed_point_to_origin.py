"""
Given a list of points and an integer k, return
the k points closest to the origin (0,0).

Example:
  Input:  points=[[1,3],[-2,2]], k=1
  Output: [[-2,2]]

Constraints:
  Distance squared avoids computing a square root.
  distance^2 = x^2 + y^2
"""

import heapq
from typing import List


class Solution:
    def kClosest(
        self, points: List[List[int]], k: int
    ) -> List[List[int]]:
        # Store (dist_sq, x, y) so heap orders by distance.
        distances = [
            [x ** 2 + y ** 2, x, y]
            for x, y in points
        ]
        heapq.heapify(distances)
        result = []
        while k > 0:
            item = heapq.heappop(distances)
            result.append([item[1], item[2]])
            k -= 1
        return result
