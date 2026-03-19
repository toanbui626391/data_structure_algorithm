"""
Given a list of meeting intervals, return the
minimum number of conference rooms required.

Example:
  Input:  intervals=[[0,30],[5,10],[15,20]]
  Output: 2

Constraints:
  Min-heap of end times; pop rooms that finish
  before the next meeting starts.
"""

from heapq import heappush, heappop
from typing import List


class Solution:
    def minMeetingRooms(
        self, intervals: List[List[int]]
    ) -> int:
        # Sort by start time to process in order.
        sorted_intervals = sorted(
            intervals, key=lambda it: (it.start, it.end)
        )

        result = 0
        # Heap holds end times of active meetings.
        end_heap = []

        for interval in sorted_intervals:
            start, end = interval.start, interval.end

            # Free rooms whose meetings have ended.
            while end_heap and end_heap[0] <= start:
                heappop(end_heap)

            heappush(end_heap, end)
            result = max(result, len(end_heap))

        return result
