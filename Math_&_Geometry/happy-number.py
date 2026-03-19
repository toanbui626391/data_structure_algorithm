"""
A happy number is defined by replacing the
number repeatedly with the sum of squares of
its digits until it reaches 1 (happy) or loops
forever (not happy).

Example:
  Input:  n=19
  Output: True

Constraints:
  Track visited values; a cycle means the number
  is not happy.
"""


class Solution:
    def isHappy(
        self, n: int, visited=None
    ) -> bool:
        if visited is None:
            visited = set()

        if n == 1:
            return True
        if n in visited:
            return False

        visited.add(n)
        # Sum squares of each digit to get next value.
        next_n = sum(
            int(digit) ** 2 for digit in str(n)
        )
        return self.isHappy(next_n, visited)
