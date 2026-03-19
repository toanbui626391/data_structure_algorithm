"""
Given an integer array height of length n, find
two lines that form a container holding the most
water. Return the maximum amount of water.

Example:
  Input:  height=[1,8,6,2,5,4,8,3,7]
  Output: 49

Constraints:
  area = (r - l) * min(height[l], height[r])
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height:
            return 0

        max_area = 0
        left, right = 0, len(height) - 1
        while left < right:
            max_area = max(
                max_area,
                (right - left) * min(height[left], height[right]),
            )
            # Move the shorter wall to find a potentially taller one.
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
        return max_area
