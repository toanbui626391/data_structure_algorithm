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


from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # 1. Sort by end time: O(n log n)
        intervals.sort(key=lambda x: x[1])
        
        count_kept = 0
        last_end_time = float('-inf')
        
        # 2. Greedy selection: O(n)
        for start, end in intervals:
            if start >= last_end_time:
                # No overlap, keep this interval
                count_kept += 1
                last_end_time = end
            # Else: it overlaps, so we "skip" (remove) it
                
        # 3. Result is total minus those we managed to keep
        return len(intervals) - count_kept
