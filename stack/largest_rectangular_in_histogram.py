# problem understanding
#
# strategy to solve the problem
#     maxArea (int): to hold the current max value
#     stack (index, height): to hold stack of index and height value
#
# why using stack
#     stack (start, height): keep record of increase hights when we meet lower
#     hight we can calculate area form by column of the pop stack
#     max_area (int): to keep the current max area
#     start = i: to keep the start index of col and
##########################################reference solution
from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea

    def largestRectangleArea(self, heights: List[int]) -> int:
        # Append a 0-height bar to force calculation of all remaining bars
        # This acts as a sentinel
        heights.append(0)
        # The stack will store indices.
        # We add -1 as a base sentinel to simplify width calculation.
        stack = [-1]
        max_area = 0
        for i in range(len(heights)):
            # We process bars when we find a bar shorter than the one 
            # at the top of the stack.
            # This new, shorter bar is the "right boundary".
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                # This is the bar for which we are calculating the max area
                h = heights[stack.pop()]
                # stack[-1] is now the "left boundary"
                # i is the "right boundary"
                w = i - stack[-1] - 1
                max_area = max(max_area, h * w)
            # Push the current index onto the stack
            stack.append(i)            
        # Remove the sentinel bar we added (good practice, though not strictly needed)
        heights.pop()        
        return max_area          