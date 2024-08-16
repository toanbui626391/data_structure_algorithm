"""
strategy to solve the problem
    problem: climb stars with cost associate. you can climb on or two step and have to pay the associate cost of the staircase
    why:
        d[i] is the min cost you pay at index i
        dp[i] = min(cost[i] + dp[i-1], cost[i]+dp[i-2])
        return min(dp[-1], dp[-2]) #you can reach the last index by the last index or the second last

"""

"""
Recursive style with depth first search and memorization
    We must draw decision tree to see dfs threverse the tree and collect cost
"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        @cache
        def dfs(i):
            if i >= len(cost):
                return 0
            return cost[i] + min(dfs(i+1), dfs(i+2))
        return min(dfs(0), dfs(1)) #start from 0, or 1
    

"""
Dynamic Programing style:
    dynamic programing style is also derived from dfs search problem
"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)
        if n <= 2:
            return min(cost)
        cur, prev = 0, 0
        for c in cost:
            cur, prev = c + min(cur, prev), cur
        return min(cur, prev)
