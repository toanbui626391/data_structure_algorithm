"""
Reverse the bits of a given 32-bit unsigned
integer.

Example:
  Input:  n=43261596 (binary: 00000010...)
  Output: 964176192

Constraints:
  Build result bit by bit: left-shift result to
  make room, then OR in the lowest bit of n,
  then right-shift n.
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            # Shift result left; add current lowest bit.
            result = (result << 1) | (n & 1)
            # Advance to next bit of n.
            n >>= 1
        return result
