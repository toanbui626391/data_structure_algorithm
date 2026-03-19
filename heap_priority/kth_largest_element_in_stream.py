"""
Design a class to find the kth largest element in
a stream. add(val) adds val and returns the kth
largest element.

Example:
  KthLargest(3,[4,5,8,2]); add(3)->4; add(5)->5

Constraints:
  A min-heap of size k keeps the kth largest at the root.
"""

import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Build and trim the heap to size k at init time.
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        # Push and maintain heap size at k.
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        # Root of min-heap is the kth largest.
        return self.nums[0]
