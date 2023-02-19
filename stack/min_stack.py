#problem understanding
    #Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

#strategy to solve the problem
    #maintain two stack (normal stack and min stack)
        #stack to keep elements
        #minStack to keep current min value of stack. in this way, went pop or push any value it will allways keep the information about min value of stack
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