"""
Given a list of costs per stair, find the minimum
cost to reach the top. You can start at step 0 or
step 1 and take 1 or 2 steps each time.

Example:
  Input:  cost=[10,15,20]
  Output: 15

Constraints:
  dp[i] = cost[i] + min(dp[i-1], dp[i-2]).
"""

from typing import List


class Solution:
    def minCostClimbingStairs(
        self, cost: List[int]
    ) -> int:
        num_stairs = len(cost)
        if num_stairs <= 2:
            return min(cost)
        # Rolling variables track the two most recent dp values.
        current = 0
        previous = 0
        for step_cost in cost:
            current, previous = (
                step_cost + min(current, previous),
                current,
            )
        return min(current, previous)
