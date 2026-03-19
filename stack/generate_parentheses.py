"""
Given n pairs of parentheses, generate all
combinations of well-formed parentheses.

Example:
  Input:  n=3
  Output: ["((()))","(()())","(())()","()(())","()()()"]

Constraints:
  num_open >= num_close to keep the string well-formed.
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(num_open, num_close, current_string):
            # A valid combo has exactly n of each bracket.
            if num_open == num_close == n:
                result.append(current_string)
                return
            # Add an open bracket while budget remains.
            if num_open < n:
                dfs(num_open + 1, num_close, current_string + "(")
            # Add a close bracket only when open count allows it.
            if num_open > num_close:
                dfs(num_open, num_close + 1, current_string + ")")

        result = []
        dfs(0, 0, "")
        return result
