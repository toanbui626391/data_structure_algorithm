"""
strategy to solve the problem:
    problem:

"""
class Solution:
    def rob(self, nums: List[int]) -> int:

        def rob_house(nums):
            #dynamic programming
            dp = [0] * len(nums)
            dp[0], dp[1] = nums[0], max(nums[0], nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i-1], nums[i]+dp[i-2])
            return dp[-1]

        #edge case for num house <= 2
        if len(nums) <= 2:
            return max(nums)
        return max(rob_house(nums[:-1]), rob_house(nums[1:]))