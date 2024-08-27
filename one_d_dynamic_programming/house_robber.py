"""
strategy to solve the problem
    problem: 
        given a list of house with house value. you are professional robber by try to maximize total value robbed. One contraint is that robber can not rob two days in a row.
    why:
        each day we will decide rob or not rob house. 
        dp[i] = max(dp[i-1], dp[i-2]+nums[i]), the max value of current day i is equal to max value of last day or do not rob the house or the last two day and rob the house today
"""

"""
Recursive and  Memorize style
    We must visualize decision tree, if you rob the current house, we can not drop next hope but can rob the next next house
"""
class Solution:
    def rob(self, nums: List[int]) -> int:

        @cache
        def dfs(i):
            if i >= len(nums):
                return 0
            return max(nums[i]+dfs(i+2), dfs(i+1))
        if len(nums) <= 2:
            return max(nums)
        return dfs(0)
    
"""
Dynamic programing style
"""    
class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) <=2:
            return max(nums)
        cur, prev = 0, 0
        for n in nums:
            cur, prev = max(n+prev, cur), cur
        return cur