class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #xor bitwise operation:
            # x^x -> 0
            # x^y = y^x
            # x^0 = x
        # because run two loop multiplication to find answer  
        n = len(nums)
        ans = 0
        for i in range(1, n + 1):
            ans ^= i
        for num in nums:
            ans ^= num
        return ans
