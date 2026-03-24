"""
Problem: Min Stack

Design a stack that supports push, pop, top, and
retrieving the minimum element in constant time.

Example:
  MinStack()
  push(-2); push(0); push(-3);
  getMin() -> -3
  pop()
  top() -> 0
  getMin() -> -2

Approach: Two Stacks
  - main_stack: stores the actual values.
  - min_stack: stores the minimum value seen so
    far up to that parallel depth.
"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        # Determine the new minimum at this level
        if self.min_stack:
            current_min = min(val, self.min_stack[-1])
        else:
            current_min = val
            
        self.min_stack.append(current_min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
