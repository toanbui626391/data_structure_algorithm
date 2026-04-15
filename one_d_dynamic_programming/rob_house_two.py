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


def rob_two_optimized(nums: List[int]) -> int:
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    def rob_linear(data: List[int]) -> int:
        if len(data) <= 2:
            return max(data)

        # Variables representing dp[i-2] and dp[i-1]
        two_houses_back = data[0]
        one_house_back = max(data[0], data[1])

        # Iterate from house 3 up to n
        for i in range(2, len(data)):
            # Max of robbing current vs skip
            current = max(
                one_house_back,
                two_houses_back + data[i],
            )

            # Shift variables forward
            two_houses_back = one_house_back
            one_house_back = current

        return one_house_back

    # Compare [0..n-2] vs [1..n-1] for the circle.
    return max(
        rob_linear(nums[:-1]),
        rob_linear(nums[1:]),
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
