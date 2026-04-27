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
    def insert(
        self,
        intervals: List[List[int]],
        new_interval: List[int],
    ) -> List[List[int]]:
        result = []

        for interval in intervals:
            # Interval ends before the new one starts.
            if interval[1] < new_interval[0]:
                result.append(interval)
            
            # Interval starts after the new one ends.
            elif interval[0] > new_interval[1]:
                result.append(new_interval)
                new_interval = interval
            
            # Intervals overlap, so merge them together.
            else:
                new_start = min(
                    interval[0], new_interval[0]
                )
                new_end = max(
                    interval[1], new_interval[1]
                )
                new_interval = [new_start, new_end]

        # Append the final merged or remaining interval.
        result.append(new_interval)
        
        return result


if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    intervals_1 = [[1, 3], [6, 9]]
    new_interval_1 = [2, 5]
    
    res_1 = sol.insert(intervals_1, new_interval_1)
    
    print("Test 1:")
    print(f"Input: {intervals_1}, {new_interval_1}")
    print(f"Output: {res_1}")
    print()

    # Test case 2
    intervals_2 = [
        [1, 2], [3, 5], [6, 7], [8, 10], [12, 16]
    ]
    new_interval_2 = [4, 8]
    
    res_2 = sol.insert(intervals_2, new_interval_2)
    
    print("Test 2:")
    print(f"Input: {intervals_2}, {new_interval_2}")
    print(f"Output: {res_2}")
