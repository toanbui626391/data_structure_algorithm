"""
Given an array of heights representing a histogram
where each bar has width 1, find the area of the
largest rectangle in the histogram.

Example:
  Input:  heights=[2,1,5,6,2,3]
  Output: 10

Constraints:
  A monotonic stack tracks increasing bars and computes
  rectangle area when a shorter bar is encountered.
"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # A sentinel bar forces remaining bars to be processed.
        heights.append(0)
        # Stack stores indices; -1 is a sentinel left boundary.
        stack = [-1]
        max_area = 0
        for i in range(len(heights)):
            # Process all bars taller than the current one.
            while (
                stack[-1] != -1
                and heights[stack[-1]] >= heights[i]
            ):
                # Height of the popped bar.
                height = heights[stack.pop()]
                # Width is bounded by new top and current index.
                width = i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        heights.pop()
        return max_area
