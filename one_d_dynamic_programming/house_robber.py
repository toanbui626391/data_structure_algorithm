"""
Given a list of house values, return the maximum
amount that can be robbed without robbing two
adjacent houses.

Example:
  Input:  nums=[2,7,9,3,1]
  Output: 12

Constraints:
  dp[i] = max(dp[i-1], dp[i-2] + nums[i]).
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        # Rolling variables track the previous two dp values.
        current = 0
        previous = 0
        for value in nums:
            current, previous = (
                max(value + previous, current),
                current,
            )
        return current
