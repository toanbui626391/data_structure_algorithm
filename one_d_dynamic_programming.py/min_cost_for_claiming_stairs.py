"""
startegy to solve the problem
    problem: given a list of costs for each stair case. for each steps you can move one or two staircase and pay cost[i]. compute the min cost to claim that stair
    why:
        using dinamic programming with compute from the bottom of decision tree.
"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #start from the third staircase. because we know value for the two last stair case and go back to the decision tree
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1]) #check the cost of take one or two step at root
