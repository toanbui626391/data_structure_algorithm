"""
strategy to solve the problem:
    problem:

"""
"""
Recursive and Memorization style
    add robFirst to track when to stop traverse the tree
"""
class Solution:
    def rob(self, nums):

        @cache
        def dfs(i, robFirst):
            n = len(nums)
            if i >= n or (i >= n-1 and robFirst):
                return 0
            return max(nums[i]+dfs(i+2, robFirst), dfs(i+1, robFirst))
        
        if len(nums) < 2:
            return max(nums)
        return max(dfs(1, False), nums[0] + dfs(2, True))
    

class Solution:
    def rob(self, nums):

        def rob_helper(data):
            n = len(data)
            if n <= 2:
                return max(data)
            cur, prev = 0, 0
            for n in data:
                cur, prev = max(n+prev, cur), cur
            return cur
        if len(nums) < 2:
            return max(nums)
        return max(rob_helper(nums[:-1]), rob_helper(nums[1:]))
