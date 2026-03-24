# Stack Data Structure

## What Is It?

A **Stack** is a linear data structure that
follows the Last-In-First-Out (LIFO) principle.
The last element added is the first one to be
removed.

You can think of it like a stack of cafeteria
plates: you add plates to the top and you must
remove plates from the top.

---

## Core Idea

The core idea of a stack is to provide a way to
temporarily hold data that needs to be accessed
in reverse order.

It acts as a "memory" of unresolved tasks. When
processing a sequence of items, you push data
that you aren't ready to handle onto the stack.
Later, when a resolving condition arrives, you
pop the data back off the stack to process it.

---

## Why Is It Used?

1. **Efficiency:** Push and pop operations are
   both O(1) constant time in Python.
2. **Order Reversal:** It naturally reverses
   the order of elements.
3. **Simulating Recursion:** It converts
   recursive function calls (which inherently
   use the system call stack) into an iterative
   solution (using an explicit stack).

---

## General Implementation (Python)

In Python, a standard `list` is structurally
optimized to act as a stack. We use `.append()`
to push and `.pop()` to pop.

### Basic Stack Operations

```python
stack = []

# 1. PUSH (O(1))
stack.append(1)
stack.append(2)

# 2. PEEK / View Top (O(1))
top = stack[-1]  # top is 2

# 3. POP (O(1))
val = stack.pop()  # returns 2

# 4. CHECK IF EMPTY (O(1))
if not stack:
    pass # stack is empty
```

### The "Monotonic Stack" Template

A popular algorithm variant is the monotonic
stack, used to find the "Next Greater Element."

```python
def next_greater_element(arr):
    res = [-1] * len(arr)
    # Stores indices of unresolved items
    stack = []

    for i in range(len(arr)):
        # While current element resolves items
        # sitting on top of the stack:
        while stack and arr[i] > arr[stack[-1]]:
            popped_idx = stack.pop()
            res[popped_idx] = arr[i]
        
        # Push current unresolved item
        stack.append(i)

    return res
```

---

## Suitable Problem Types

### 1. Matching and Validation
- **Valid Parentheses:** Push opening brackets.
  When a closing bracket arrives, pop and check
  if it matches the expected bracket type.

### 2. Expression Evaluation
- **Reverse Polish Notation (RPN):** Push
  numbers. When an operator arrives, pop the
  last two numbers, apply the operator, and
  push the result back.

### 3. Monotonic Sequence Finding
- **Next Greater/Smaller Element:** Used heavily
  in problems like "Daily Temperatures".
- **Largest Rectangle in Histogram:** Use a
  monotonic stack to track heights that haven't
  yet found their smaller right boundaries.

### 4. Tree and Graph Traversal
- **Iterative DFS:** Replace recursion with an
  explicit stack to explore branching paths
  deeply before backtracking.
