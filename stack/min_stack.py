#problem understanding
    #Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

#strategy to solve the problem
    #maintain two stack (normal stack and min stack)
        #stack to keep elements
        #minStack to keep min of the current index of normal stack
#################################reference solution
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]