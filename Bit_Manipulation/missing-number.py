"""
Given an array of n distinct numbers in [0, n],
return the one missing number.

Example:
  Input:  nums=[3,0,1]
  Output: 2

Constraints:
  XOR every index 1..n with every element;
  duplicate values cancel, leaving the missing one.
"""

from typing import List


class Solution:
  def missingNumber(nums):
      missing = len(nums)
      for i, num in enumerate(nums):
          missing ^= i ^ num
      return missing
