class Solution:
    @cache
    def myPow(self, x: float, n: int) -> float:
        #base c
        if n == 0:
            return 1
        elif n < 0:
            return 1 / (x * self.myPow(x, -n - 1))
        elif n % 2 == 0:
            self.myPow(x, n // 2) * self.myPow(x, n//2)
        return x * self.myPow(x, n - 1)