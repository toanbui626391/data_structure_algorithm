"""
Problem: Container With Most Water

Given an integer array height of length n, find
two lines that form a container holding the most
water. Return the maximum amount of water.

Example:
  Input:  height=[1,8,6,2,5,4,8,3,7]
  Output: 49

Approach: Two Pointers (Converging)
  - Area = width * min(height[left], height[right])
  - Start pointers at both ends (max width).
  - Move the pointer pointing to the shorter line
    inward, hoping to find a taller line to
    compensate for the reduced width.
"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height:
            return 0

        max_area = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            # Calculate current area
            width = right - left
            current_height = min(height[left], height[right])
            current_area = width * current_height
            
            max_area = max(max_area, current_area)
            
            # Move the shorter wall inward to find a
            # potentially taller wall.
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area
