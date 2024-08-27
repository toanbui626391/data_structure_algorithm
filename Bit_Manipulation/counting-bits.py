class Solution:
    def countBits(self, n: int) -> List[int]:
    # x>>1 =>x/2 int division
    # x<<1 =>x*2
    # x&1  => is_odd(x)
    # 1<<b =>2**b
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans