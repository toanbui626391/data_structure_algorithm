"""
You have an array of stones. Each turn, smash the
two heaviest together. If equal, both are destroyed;
otherwise the difference is put back. Return the
last remaining stone weight, or 0 if none remain.

Example:
  Input:  stones=[2,7,4,1,8,1]
  Output: 1

Constraints:
  A max-heap (negated for Python's min-heap) picks the two largest.
"""

from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Negate values to simulate a max-heap.
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            # Push remainder back if stones differ.
            if first < second:
                heapq.heappush(stones, first - second)

        # Return 0 if all stones were destroyed.
        stones.append(0)
        return abs(stones[0])
