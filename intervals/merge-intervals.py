"""
Given an array of intervals, merge all
overlapping intervals and return the result.

Example:
  Input:  intervals=[[1,3],[2,6],[8,10],[15,18]]
  Output: [[1,6],[8,10],[15,18]]

Constraints:
  Sort by start; track the last merged interval
  and extend its end when overlap is found.
"""

from typing import List


class Solution:
    def merge(
        self, intervals: List[List[int]]
    ) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()

        merged = []
        last = intervals[0]
        for curr in intervals:
            # Overlap: extend last interval's end.
            if curr[0] <= last[1]:
                last[1] = max(last[1], curr[1])
            else:
                # No overlap: save last, advance.
                merged.append(last)
                last = curr

        merged.append(last)
        return merged
