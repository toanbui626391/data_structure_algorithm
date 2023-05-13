"""
strategy to solve the problem
    problem: 
        given a list of house with house value. you are professional robber by try to maximize total value robbed. One contraint is that robber can not rob two days in a row.
    why:
        each day we will decide rob or not rob house. 
        dp[i] = max(dp[i-1], dp[i-2]+nums[i]), the max value of current day i is equal to max value of last day or do not rob the house or the last two day and rob the house today
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        #edge case, you can only rob one of the house
        if len(nums) <= 2:
            return max(nums)
        
        #dp
        L = len(nums)
        dp = [0 for _ in range(L)]
        #first day you only have one house to rob, second day you can choose between two house
        dp[0], dp[1] = nums[0], max(nums[0], nums[1]) #star with first and second day
        
        for i in range(2, L):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1]) #find max between two decision. if you rob today then you must have rob in the day before yesterday else you will not rob today[-=ppkjmmmmmmmmm]
        
        return dp[-1]