"""
Given an unsigned integer, return the number
of '1' bits (Hamming weight).

Example:
  Input:  n=11 (binary: 1011)
  Output: 3

Constraints:
  Right-shift through all 32 bits, accumulating
  the lowest bit each iteration.
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            # Lowest bit is 1 if n is odd.
            count += n & 1
            # Shift right to examine next bit.
            n >>= 1
        return count
