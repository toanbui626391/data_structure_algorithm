"""
Problem: Valid Parentheses

Given a string s containing only '(', ')', '{',
'}', '[', ']', determine if the input is valid.
Open brackets must be closed by the same type of
brackets and in the correct order.

Example:
  Input:  s="()[]{}"
  Output: True

Approach: Stack
  - Use a stack to keep track of opening brackets.
  - Map each closing bracket to its matching
    opening bracket.
  - If we see an opening bracket, push it.
  - If we see a closing bracket, the top of the
    stack MUST be its matching opening bracket.
    Otherwise, the string is invalid.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        # Map closing brackets to opening brackets
        match = {")": "(", "]": "[", "}": "{"}
        stack = []

        for char in s:
            # 1. If it's a closing bracket
            if char in match:
                # Top of stack must be its opener
                if stack and stack[-1] == match[char]:
                    stack.pop()
                else:
                    return False
            
            # 2. If it's an opening bracket
            else:
                stack.append(char)

        # 3. Valid strings leave an empty stack
        return len(stack) == 0


if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("()"))      # True
    print(sol.isValid("()[]{}"))  # True
    print(sol.isValid("(]"))      # False
    print(sol.isValid("([)]"))    # False
