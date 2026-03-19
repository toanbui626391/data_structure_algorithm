"""
Implement pow(x, n), which calculates x raised
to the power n.

Example:
  Input:  x=2.00000, n=10
  Output: 1024.00000

Constraints:
  Recursive: negative n inverts; even n halves
  the exponent; odd n multiplies by x and
  recurses with n-1.
"""

from functools import cache


class Solution:
    @cache
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1 / (x * self.myPow(x, -n - 1))
        if n % 2 == 0:
            return (
                self.myPow(x, n // 2)
                * self.myPow(x, n // 2)
            )
        return x * self.myPow(x, n - 1)
