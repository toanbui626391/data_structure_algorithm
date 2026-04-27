"""
Problem:
Given a sorted list of non-overlapping intervals
and a new interval, insert it in order, merging
any overlapping intervals.

Examples:
Input:
  intervals = [[1, 3], [6, 9]]
  new_interval = [2, 5]
Output:
  [[1, 5], [6, 9]]

Constraints:
0 <= intervals.length <= 10^4
intervals[i].length == 2
"""

from typing import List


class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = []
        
        for i, interval in enumerate(intervals):
            # Case 1: newInterval is completely before the current interval
            if newInterval[1] < interval[0]:
                result.append(newInterval)
                # We can return immediately by concatenating the rest of the list
                return result + intervals[i:]
            
            # Case 2: newInterval is completely after the current interval
            elif newInterval[0] > interval[1]:
                result.append(interval)
                
            # Case 3: Overlap exists, merge them into newInterval
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
                
        # If we loop through the whole array without triggering Case 1,
        # the newInterval (or the merged mega-interval) goes at the very end.
        result.append(newInterval)
        
        return result
