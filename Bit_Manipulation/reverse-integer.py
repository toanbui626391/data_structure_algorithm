"""
Given a 32-bit signed integer, reverse its
digits. Return 0 if the result overflows.

Example:
  Input:  x=123
  Output: 321

Constraints:
  Check for overflow before building each digit;
  use 2^31 as the overflow boundary.
"""


class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        sign = 1 if x >= 0 else -1

        # 2^31; max valid 32-bit value is 2^31 - 1.
        int_max = 1 << 31
        max_head = int_max // 10
        max_tail = int_max % 10

        x = abs(x)
        while x > 0:
            remainder = x % 10
            # Stop if adding this digit would overflow.
            if result > max_head or (
                result == max_head
                and remainder >= max_tail
            ):
                return 0
            result = (result * 10) + remainder
            x //= 10

        return result * sign
