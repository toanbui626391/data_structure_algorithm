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
"""
Recursive and Memorization style
    You need to draw decision tree in which you can take 1, or 2 step
    the goal is to reach to the top of the step. We can reach to the top (correct) or pass over it (not correct)
"""
class Solution:
    def climbStairs(self, n: int) -> int:

        @cache
        def dfs(steps: int):
            if steps == n:
                return 1
            elif steps > n:
                return 0
            return dfs(steps+1) + dfs(steps+2)
        return dfs(0)
    
"""
Dynamic Programing Style
    Dynamic programing style is derived from dfs recursion tree. We notic that f(n) = f(n+1) + f(n+2).
    Because you can take 1 or 2 step
"""
class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 2:
            return n
        cur, prev = 1, 1
        for i in range(2, n+1):
            cur, prev = cur+prev, cur
        return cur  