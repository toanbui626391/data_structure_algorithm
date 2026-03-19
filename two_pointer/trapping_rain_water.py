"""
Given n non-negative integers representing an
elevation map where each bar has width 1, compute
how much water can be trapped after raining.

Example:
  Input:  height=[0,1,0,2,1,0,1,3,2,1,2,1]
  Output: 6

Constraints:
  Water trapped at index i = min(maxLeft, maxRight) - height[i].
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max = height[left]
        right_max = height[right]
        result = 0
        while left < right:
            # Process whichever side has the smaller max first.
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                result += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                result += right_max - height[right]
        return result
