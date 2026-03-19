"""
Given two non-negative integers as strings,
return their product as a string without using
built-in big-integer libraries or converting
inputs directly to int.

Example:
  Input:  num1="2", num2="3"
  Output: "6"

Constraints:
  Parse each string manually by digit position,
  then multiply the resulting integers.
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(
            self._parse(num1) * self._parse(num2)
        )

    def _parse(self, num_str: str) -> int:
        result = 0
        for i in range(len(num_str)):
            # Build integer digit by digit.
            result = (
                result * 10
                + ord(num_str[i]) - ord('0')
            )
        return result
