"""
Design a MedianFinder that supports addNum and
findMedian. findMedian returns the median of all
numbers added so far.

Example:
  addNum(1); addNum(2); findMedian() -> 1.5
  addNum(3); findMedian() -> 2.0

Constraints:
  Two heaps (max for lower half, min for upper half) give O(log n)
  insertion and O(1) median.
"""

import heapq


class MedianFinder:
    def __init__(self):
        """
        Initialize with an empty lower and upper heap.
        """
        # small is a max-heap (negated); large is a min-heap.
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        # Route to large heap if num belongs in upper half.
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)

        # Rebalance so sizes differ by at most 1.
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2
