# Backtracking

## What is Backtracking?
Backtracking is an algorithmic technique for
solving problems by building a solution
incrementally. It explores choices one at a
time, and as soon as it determines a choice
cannot lead to a valid solution, it **undoes**
that choice (backtracks) and tries the next one.

It is essentially a controlled, pruned form of
brute-force search over a decision tree.

---

## Core Idea
Every backtracking solution follows the same
three-step pattern at each decision point:

1. **Choose:** Make a choice (add to path).
2. **Explore:** Recurse with updated state.
3. **Un-choose:** Undo the choice (remove
   from path) before trying the next option.

```
# Standard backtracking template

def backtrack(state, choices):
    if is_solution(state):
        results.append(state[:])
        return

    for choice in choices:
        if is_valid(choice, state):
            # 1. Choose
            state.add(choice)
            # 2. Explore
            backtrack(state, next_choices)
            # 3. Un-choose
            state.remove(choice)
```

The key insight: state is **modified in place**
before recursing and **restored** after. This
avoids creating a copy of state at every level.

---

## Common Problem Patterns

### 1. Subsets / Power Set
Generate all subsets of a list.
The choice at each step: include or skip.

```python
def subsets(nums):
    results = []

    def backtrack(start, path):
        # Every path is a valid subset.
        results.append(path[:])
        for i in range(start, len(nums)):
            # Choose
            path.append(nums[i])
            # Explore
            backtrack(i + 1, path)
            # Un-choose
            path.pop()

    backtrack(0, [])
    return results
```

---

### 2. Permutations
Generate all orderings of a list.
The choice at each step: pick any unused element.

```python
def permutations(nums):
    results = []

    def backtrack(path, used):
        if len(path) == len(nums):
            results.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            # Choose
            used[i] = True
            path.append(nums[i])
            # Explore
            backtrack(path, used)
            # Un-choose
            path.pop()
            used[i] = False

    backtrack([], [False] * len(nums))
    return results
```

---

### 3. Combinations
Pick k elements from n without repetition.
Use a `start` index to avoid revisiting.

```python
def combine(n, k):
    results = []

    def backtrack(start, path):
        if len(path) == k:
            results.append(path[:])
            return
        for i in range(start, n + 1):
            # Choose
            path.append(i)
            # Explore
            backtrack(i + 1, path)
            # Un-choose
            path.pop()

    backtrack(1, [])
    return results
```

---

## Pruning
Pruning is what separates backtracking from
pure brute force. By adding an `if is_valid`
guard before recursing, you cut off entire
branches of the search tree early.

Example: in a Sudoku solver, before placing a
number, check if it is valid in its row, column,
and 3x3 box. If not, skip it immediately instead
of recursing into thousands of useless states.

---

## Complexity
Backtracking is generally **exponential** in
the worst case, as it explores all possibilities.
Pruning reduces the average case significantly
but not the worst case.

- Subsets: O(2^n)
- Permutations: O(n!)
- Combinations: O(n choose k)

Space is O(n) for the recursion call stack
(depth of the decision tree).
