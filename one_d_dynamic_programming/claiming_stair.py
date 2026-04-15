"""
Count the number of distinct ways to climb n stairs,
taking 1 or 2 steps at a time.

Example:
  Input:  n=3
  Output: 3  (1+1+1, 1+2, 2+1)

Constraints:
  dp[n] = dp[n-1] + dp[n-2] because each step comes from 1 or 2 below.
"""

from functools import cache


def climbStairs_optimized(n: int) -> int:
    if n <= 2:
        return n
        
    # Variables representing dp[i-2] and dp[i-1]
    two_steps_back = 1
    one_step_back = 2
    
    # Iterate from step 3 up to n
    for i in range(3, n + 1):
        # Calculate current step
        current = one_step_back + two_steps_back
        
        # Shift variables forward for the next iteration
        two_steps_back = one_step_back
        one_step_back = current
        
    return one_step_back

# Standard 1D top-down DP with memoization.
# Key idea:
#   - Use a dictionary to store previously
#     computed results for a given `n`.
#   - Check the `memo` before recursing.
class SolutionMemo:
    def climbStairs(
        self, n: int, memo: dict[int, int] = None
    ) -> int:
        if memo is None:
            memo = {}

        # Check if result is already in cache
        if n in memo:
            return memo[n]

        # Base cases
        if n <= 2:
            return n

        # Recursive step with memoization
        memo[n] = (
            self.climbStairs(n - 1, memo)
            + self.climbStairs(n - 2, memo)
        )

        return memo[n]


if __name__ == "__main__":
    sol = SolutionMemo()

    # n=1 -> 1 way
    print(sol.climbStairs(1))

    # n=2 -> 2 ways (1+1, 2)
    print(sol.climbStairs(2))

    # n=3 -> 3 ways (1+1+1, 1+2, 2+1)
    print(sol.climbStairs(3))

    # n=5 -> 8 ways
    print(sol.climbStairs(5))
