"""
Given an array of intervals, return the minimum
number of intervals to remove so the rest do
not overlap.

Example:
  Input:  intervals=[[1,2],[2,3],[3,4],[1,3]]
  Output: 1

Constraints:
  Find the longest non-overlapping sequence via
  memoized DP, then subtract from total count.
"""

from functools import cache
from typing import List


class Solution:
    def eraseOverlapIntervals(
        self, intervals: List[List[int]]
    ) -> int:
        intervals = sorted(intervals)

        @cache
        def dp(idx):
            # Find longest non-overlapping chain.
            curr_start, curr_end = intervals[idx]
            for pos in range(idx + 1, len(intervals)):
                next_start, next_end = intervals[pos]
                # No overlap: extend chain.
                if curr_end <= next_start:
                    return 1 + dp(pos)
                # Contained: skip contained interval.
                if curr_end > next_end:
                    return dp(pos)
            return 1

        # Removals = total minus longest kept chain.
        return len(intervals) - dp(0)
