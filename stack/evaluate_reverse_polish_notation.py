"""
Evaluate an arithmetic expression in Reverse Polish
Notation. Valid operators are +, -, *, /. Division
truncates toward zero.

Example:
  Input:  tokens=["2","1","+","3","*"]
  Output: 9

Constraints:
  A stack provides the two most recent operands for each op.
"""

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char == "+":
                stack.append(stack.pop() + stack.pop())
            elif char == "-":
                first, second = stack.pop(), stack.pop()
                stack.append(second - first)
            elif char == "*":
                stack.append(stack.pop() * stack.pop())
            elif char == "/":
                first, second = stack.pop(), stack.pop()
                # int() truncates toward zero.
                stack.append(int(second / first))
            else:
                stack.append(int(char))
        return stack[0]
