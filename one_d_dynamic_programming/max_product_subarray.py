"""
the strategy to solve problem
    problem:
        given a list of number nums. compute max product of subarrays
    why:
        using dynamic programming for a subarray problem
        max product of subarray, we want subarray to largest. But we have negative int in array
        we solve it by keep track of curMin, curMax
        val = (n, n*curMin, n*curMax) and curMin, curMax = min(val), max(val) to switch the subarray when have negative int
"""
import math
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #for a max p
        curMin, curMax = 1, 1
        res = nums[0]
        for n in nums:
            val = (n, n*curMin, n*curMax)
            curMin, curMax = min(val), max(val)
            res = max(res, curMax)
        return res
    
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        self.memo = {}
        def dfs(i, currentProduct):
            key = (i, currentProduct)
            if (key in self.memo):
                return self.memo[key]
            if (i >= len(nums)):
                return currentProduct
			# 3 choices, Include the current number in the product, start a new product, or end the product
            ans = max(dfs(i + 1, currentProduct * nums[i]), dfs(i + 1, nums[i]), currentProduct)
            self.memo[key] = ans
            return ans
        return dfs(1, nums[0])