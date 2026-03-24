"""
Problem: Generate Parentheses

Given n pairs of parentheses, generate all
combinations of well-formed parentheses.

Example:
  Input:  n = 3
  Output: ["((()))","(()())","(())()",
           "()(())","()()()"]

Approach: Backtracking / Stack (Implicit)
  - Add an open bracket if open_count < n.
  - Add a close bracket if close_count < open_count.
  - A valid combination is formed when
    open_count == close_count == n.
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(open_n, closed_n, path):
            # Base case: we've used all brackets
            if open_n == n and closed_n == n:
                res.append(path)
                return

            # We can always add an open bracket if
            # we haven't reached the limit (n).
            if open_n < n:
                backtrack(open_n + 1, closed_n, path + "(")

            # We can only add a closed bracket if
            # it matches an already open bracket.
            if closed_n < open_n:
                backtrack(open_n, closed_n + 1, path + ")")

        backtrack(0, 0, "")
        return res
