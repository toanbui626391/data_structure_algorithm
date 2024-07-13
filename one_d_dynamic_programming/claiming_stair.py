"""
strategy to solve the problem
    problem
        claiming the stair which have n step. each time you can take 1 or 2 step. compute number of distince way to climb on the top
    why:
        using dynamic programming
            f(1)= 1. stairs with 1 we want go by on step
            f(2)= 2. starirs with 2 we can go with 1+1 or 2.
        dp[i] = dp[i-1] + dp[i-2] means the number of way to reach i equal number of way to reach i-1 + i-2 because you eighter take one or two step to reach i
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        #using top down approach.
        if n <= 2:
            return n
        dp = [0] * n
        dp[0], dp[1] = 1, 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]