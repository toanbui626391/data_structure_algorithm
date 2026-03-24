"""
Problem: Evaluate Reverse Polish Notation

Evaluate an arithmetic expression in Reverse
Polish Notation (RPN). Valid operators are
+, -, *, /. Division truncates toward zero.

Example:
  Input:  tokens = ["2","1","+","3","*"]
  Output: 9  ((2 + 1) * 3)

Approach: Stack
  - Push numbers onto the stack.
  - When seeing an operator, pop the top two
    numbers, evaluate them, and push the
    result back onto the stack.
  - Order matters for subtraction and division!
"""

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                b = stack.pop()
                a = stack.pop()
                # int() truncates toward zero in Python
                stack.append(int(a / b))
            else:
                stack.append(int(token))
                
        return stack[0]
