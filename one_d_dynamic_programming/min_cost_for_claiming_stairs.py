"""
strategy to solve the problem
    problem: climb stars with cost associate. you can climb on or two step and have to pay the associate cost of the staircase
    why:
        d[i] is the min cost you pay at index i
        dp[i] = min(cost[i] + dp[i-1], cost[i]+dp[i-2])
        return min(dp[-1], dp[-2]) #you can reach the last index by the last index or the second last

"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #edge case
        if len(cost) <= 2:
            return min(cost)
        #dp
        dp = [0] * len(cost)
        dp[0], dp[1] = cost[0], cost[1] #because we can start at index 0 or index 1
        for i in range(2, len(cost)):
            dp[i] = min(dp[i-1]+cost[i], cost[i]+dp[i-2])
        return min(dp[-1], dp[-2])
