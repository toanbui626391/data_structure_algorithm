"""
Given a string s containing only '(', ')', '{',
'}', '[', ']', determine if the input is valid.
Open brackets must be closed in the correct order.

Example:
  Input:  s="()[]{}"
  Output: True

Constraints:
  A stack of open brackets is emptied by matching closes.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        # Map each closing bracket to its matching opener.
        bracket_map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for char in s:
            if char not in bracket_map:
                stack.append(char)
                continue
            # Closing bracket must match the top open bracket.
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()

        # A valid string leaves no unmatched openers.
        return not stack
