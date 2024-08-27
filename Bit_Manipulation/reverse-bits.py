class Solution:
    def reverseBits(self, n: int) -> int:

        res = 0
        for i in range(32):
            #(res << 1) or left shift with 1 -> current position to find bit
            #(n&1) -> to find last bit is 0 or 1
            #(res << 1) | (n&1) -> add found last bit to current index
            #n>>1 -> move to next bit
            res = (res << 1) | (n&1)
            n >>= 1
        return res
        