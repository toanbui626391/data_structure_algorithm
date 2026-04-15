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


def rob_optimized(nums: List[int]) -> int:
    if not nums:
        return 0
    if len(nums) <= 2:
        return max(nums)

    # Variables representing dp[i-2] and dp[i-1]
    two_houses_back = nums[0]
    one_house_back = max(nums[0], nums[1])

    # Iterate from house 3 up to n
    for i in range(2, len(nums)):
        # Calculate max if we rob current vs skip
        current = max(
            one_house_back,
            two_houses_back + nums[i],
        )

        # Shift variables forward for the next iteration
        two_houses_back = one_house_back
        one_house_back = current

    return one_house_back


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
