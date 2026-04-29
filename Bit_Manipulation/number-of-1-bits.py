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


def hammingWeight(n):
    count = 0
    while n > 0:
        # Wipe out the lowest 1 bit
        n = n & (n - 1)
        # Increment our count of 1s found
        count += 1
    return count
