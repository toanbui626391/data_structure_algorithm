"""
Houses are arranged in a circle, so the first and
last houses are adjacent. Rob without hitting two
adjacent houses; return the maximum amount.

Example:
  Input:  nums=[2,3,2]
  Output: 3

Constraints:
  Run house-robber twice: once skipping the last house,
  once skipping the first house; take the maximum.
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        def rob_helper(data: List[int]) -> int:
            num_houses = len(data)
            if num_houses <= 2:
                return max(data)
            current = 0
            previous = 0
            for value in data:
                current, previous = (
                    max(value + previous, current),
                    current,
                )
            return current

        if len(nums) < 2:
            return max(nums)
        # Compare robbing [0..n-2] vs [1..n-1] to handle the circle.
        return max(
            rob_helper(nums[:-1]),
            rob_helper(nums[1:]),
        )
