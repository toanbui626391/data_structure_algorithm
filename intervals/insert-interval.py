"""
Given a sorted list of non-overlapping intervals
and a new interval, insert it in order, merging
any overlapping intervals.

Example:
  Input:  intervals=[[1,3],[6,9]],
          newInterval=[2,5]
  Output: [[1,5],[6,9]]

Constraints:
  One pass: append intervals before, merge
  overlapping ones, then append those after.
"""

from typing import List


class Solution:
    def insert(
        self,
        intervals: List[List[int]],
        new_interval: List[int],
    ) -> List[List[int]]:
        result = []

        for interval in intervals:
            # Current interval ends before new starts.
            if interval[1] < new_interval[0]:
                result.append(interval)
            # Current interval starts after new ends.
            elif interval[0] > new_interval[1]:
                result.append(new_interval)
                new_interval = interval
            # Intervals overlap: expand new to cover both.
            else:
                new_interval[0] = min(
                    interval[0], new_interval[0]
                )
                new_interval[1] = max(
                    new_interval[1], interval[1]
                )

        result.append(new_interval)
        return result
