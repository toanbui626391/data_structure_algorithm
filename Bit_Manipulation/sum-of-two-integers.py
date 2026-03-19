"""
Calculate the sum of two integers a and b
without using the + or - operators.

Example:
  Input:  a=1, b=2
  Output: 3

Constraints:
  XOR gives sum without carry; AND shifted left
  gives carry; repeat until carry is zero.
  Mask to 32 bits to handle Python's big integers.
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Mask keeps values within 32 bits.
        mask = (1 << 32) - 1
        while b & mask:
            # XOR adds without carry; AND<<1 is carry.
            a, b = a ^ b, (a & b) << 1
        return a & mask if b != 0 else a
