class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XOR outputs 1 if the inputs are different, and 0 if they are the same.
        # any bit that duplicate will return 0 which will not change value of sing value
        res = 0
        for n in nums:
            res ^= n
        return res