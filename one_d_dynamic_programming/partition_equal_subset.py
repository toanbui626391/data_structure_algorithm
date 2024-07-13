"""
strategy to solve the problem
    problem:
        given a list of number check whether we can divide it into two equal subset
    why:
        this is a variant of knapsack problem which choose or not choose element in subset
        if total of all elemens is odd we can not divide it into two equal subset
        dp[curr] is can be form a subset which sum is curr
        dp[curr-num] is can we form a subset which sum to curr-num
        dp[curr] = dp[curr] or dp[curr-num] #we can form a subset with thougt num or with num
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s&1: #if odd number return False
            return False
        #bitwise right shift by one equal to divide by 2 and s is even
        dp = [True]+[False]*(s>>1)
        #loop through number to choose from
        for num in nums:
            #all memory of is from 0 to s>>1 because we have dp[curr-num] then the lower bow have to be num-1 so that dp[curr-num] at least is at 0
            for curr in range(s>>1, num - 1 , -1):
                dp[curr] = dp[curr] or dp[curr-num]
        return dp[-1]