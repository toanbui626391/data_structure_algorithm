"""
Problem: Largest Rectangle in Histogram

Given an array of heights representing a histogram
where each bar has width 1, find the area of the
largest rectangle in the histogram.

Example:
  Input:  heights = [2,1,5,6,2,3]
  Output: 10

Approach: Monotonically Increasing Stack
  - Stack stores (index, height).
  - When we see a shorter bar, we pop taller bars
    because their right boundary is now fixed.
  - Calculate area for popped bars using their
    stored height and width (current index - 
    start index of the popped bar).
"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        # Stack stores tuples: (start_index, height)
        stack = []

        for i, h in enumerate(heights):
            start = i
            
            # If current height is lower than stack top,
            # pop the top and calculate its max area.
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                
                # The new bar can be extended backwards to
                # the position of the popped taller bar.
                start = index
                
            stack.append((start, h))

        # Compute areas for bars that extend to the end
        n = len(heights)
        for i, h in stack:
            max_area = max(max_area, h * (n - i))

        return max_area
