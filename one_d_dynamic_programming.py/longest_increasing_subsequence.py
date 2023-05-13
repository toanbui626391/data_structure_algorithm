"""
strategy to solve the problem
    problem:
        given a list of nums. compute the length of longest subsequence
        subsequence is array derive from array by remove some or no element without change position of elelment\
    why:
        using dynamic programming for a subarray problem
        dp[i] is the length of subarray which have left index at i
        dp[i] = max(dp[i], dp[j]+1). #
        dp[j] is the right index of subarray
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1) #count number of element in subarray which increasing
        return max(dp) #return subarray which have longest increase subarray