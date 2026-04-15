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


# Standard 1D top-down DP with memoization.
# Key idea:
#   - Similar to House Robber I, but applied
#     to two separate slices: one without the
#     first house, and one without the last.
#   - A memo cache prevents recomputation.
class SolutionMemo:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_helper(data: List[int]) -> int:
            memo = {}

            def dp(i: int) -> int:
                if i in memo:
                    return memo[i]

                if i < 0:
                    return 0

                # Max of robbing current vs skipping.
                robbed = data[i] + dp(i - 2)
                skipped = dp(i - 1)
                
                memo[i] = max(robbed, skipped)
                return memo[i]

            return dp(len(data) - 1)

        # Handle the circular condition with max:
        return max(
            rob_helper(nums[:-1]),
            rob_helper(nums[1:]),
        )


if __name__ == "__main__":
    sol = SolutionMemo()

    # Example 1 -> 3 (rob index 1)
    print(sol.rob([2, 3, 2]))

    # Example 2 -> 4 (1 + 3)
    print(sol.rob([1, 2, 3, 1]))

    # Example 3 -> 0
    print(sol.rob([0]))
