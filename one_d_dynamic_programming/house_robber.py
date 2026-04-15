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


# Standard 1D top-down DP with memoization.
# Key idea:
#   - Use a dictionary to store the max
#     robbed amount up to index `i`.
#   - Check the `memo` before recursing.
class SolutionMemo:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dp(i: int) -> int:
            # Check if result is already in cache.
            if i in memo:
                return memo[i]

            # Base cases: out of bounds.
            if i < 0:
                return 0

            # Either rob this house and skip the previous,
            # or skip this house and keep the previous max.
            memo[i] = max(
                nums[i] + dp(i - 2),
                dp(i - 1)
            )

            return memo[i]

        return dp(len(nums) - 1)


if __name__ == "__main__":
    sol = SolutionMemo()

    # Example 1 -> 4 (1 + 3)
    print(sol.rob([1, 2, 3, 1]))

    # Example 2 -> 12 (2 + 9 + 1)
    print(sol.rob([2, 7, 9, 3, 1]))
