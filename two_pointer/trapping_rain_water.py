"""
Problem: Trapping Rain Water

Given n non-negative integers representing an
elevation map where each bar has width 1, compute
how much water can be trapped after raining.

Example:
  Input:  height=[0,1,0,2,1,0,1,3,2,1,2,1]
  Output: 6

Approach: Two Pointers (Converging)
  - Water trapped at index i depends on the 
    min(maxLeft, maxRight) - height[i].
  - Use two pointers. Keep track of the running
    max for both left and right sides.
  - Advance the pointer with the smaller max, 
    since it acts as the bottleneck.
"""

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max = height[left]
        right_max = height[right]
        
        trapped_water = 0
        
        while left < right:
            # Process the smaller side first
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                trapped_water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                trapped_water += right_max - height[right]
                
        return trapped_water
