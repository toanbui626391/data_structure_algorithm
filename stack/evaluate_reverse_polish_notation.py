# problem understanding
#     You are given an array of strings tokens that represents an arithmetic
#     expression in a Reverse Polish Notation.
#     Evaluate the expression. Return an integer that represents the value of
#     the expression.
#
# strategy to solve the problem
#     using stack because we can take two most recent number
#         operation is do by sequence, result of the last operation will be
#         append to stack and then continue
#     check for operator character to do the operation
#     if character is not operator just append number
#     return is the last remaining number in the stack
#     variable:
#         stack to keep track of the two most recent numbers from tokes string
#
#     why using stack?
#         stack to keep current two value of every operation.


##########################################reference solution
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(c))
        return stack[0]