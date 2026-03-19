"""
Design a stack that supports push, pop, top, and
retrieving the minimum element in constant time.

Example:
  MinStack(); push(-2); push(0); push(-3);
  getMin() -> -3; pop(); top() -> 0; getMin() -> -2

Constraints:
  A parallel min stack always tracks the current minimum.
"""


class MinStack:
    def __init__(self):
        self.stack = []
        # Mirrors stack; each entry is the min at that depth.
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Carry the current minimum down through each push.
        val = min(
            val,
            self.min_stack[-1] if self.min_stack else val,
        )
        self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
