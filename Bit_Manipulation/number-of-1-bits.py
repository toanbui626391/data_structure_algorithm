class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        #right shift until n is 0
        while n != 0:
            # n&1 last element is 0 or 1. if 1 return 1 else 0 return 0
            count += n & 1
            #right shilt 1 position
            n >>= 1
        return count