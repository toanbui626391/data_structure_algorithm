"""
Given integer n, return an array of length n+1
where each element is the count of 1-bits in
its binary representation.

Example:
  Input:  n=5
  Output: [0,1,1,2,1,2]

Constraints:
  Right-shift halves the number; reuse the bit
  count of i//2 and add the lowest bit of i.
"""

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)
        for i in range(1, n + 1):
            # i>>1 is i//2; (i&1) is the lowest bit.
            result[i] = result[i >> 1] + (i & 1)
        return result
