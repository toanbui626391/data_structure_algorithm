"""
Given a large integer as an array of digits,
increment it by one and return the result.

Example:
  Input:  digits=[1,2,3]
  Output: [1,2,4]

Constraints:
  Traverse from the last digit; propagate carry
  by setting 9 to 0. If all were 9, prepend 1.
"""

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_digits = len(digits)
        for i in range(num_digits - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] = digits[i] + 1
                return digits
        # All digits were 9; result gains a leading 1.
        return [1] + digits
