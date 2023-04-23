#problem understanding

#stretegy to solve the proble
    #maxArea (int): to hold the current max value
    #stack (index, height): to hold stack of index and height value
#why using stack
    # stack (start, height): keep record of increase hights when we meet lower hight we can calculate area form by column of the pop stack
    # max_area (int): to keep the current max area
    # start = i: to keep the start index of col and 
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