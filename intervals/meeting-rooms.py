"""
Given a list of meeting time intervals, determine
if a person could attend all meetings (no
overlaps allowed).

Example:
  Input:  intervals=[[0,30],[5,10],[15,20]]
  Output: False

Constraints:
  Sort by start time; any consecutive overlap
  means attendance is impossible.
"""

from typing import List


class Solution:
    def canAttendMeetings(
        self, intervals: List[List[int]]
    ) -> bool:
        intervals.sort(
            key=lambda itv: (itv.start, itv.end)
        )
        for i in range(1, len(intervals)):
            # Overlap if next starts before prev ends.
            if (
                intervals[i].start
                < intervals[i - 1].end
            ):
                return False
        return True
