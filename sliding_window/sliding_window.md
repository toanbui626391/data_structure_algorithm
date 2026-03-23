# Sliding Window Algorithm

## What Is Sliding Window?

A sliding window is a sub-array (or sub-string)
that moves over a larger array (or string) from
left to right. Instead of recomputing the answer
from scratch for every position, we maintain a
window and update it incrementally.

This reduces time complexity from O(n²) or O(n³)
down to O(n) in most cases.

---

## Core Idea

Maintain two pointers, `left` and `right`, that
define the current window `[left, right]`.

- Expand the window by moving `right` forward.
- Shrink the window by moving `left` forward
  when a constraint is violated.
- Track the best answer seen so far.

---

## Two Variants

### Fixed-Size Window

The window size `k` is given. Slide it one step
at a time across the array.

```
window = arr[0..k-1]
for right in range(k, n):
    add arr[right] to window
    remove arr[right - k] from window
    update answer
```

- **Use when:** problem specifies an exact
  window size.

### Variable-Size Window

The window grows or shrinks based on a condition.

```
left = 0
for right in range(n):
    # expand: include arr[right]
    while condition_violated:
        # shrink: exclude arr[left]
        left += 1
    update answer with window [left..right]
```

- **Use when:** problem asks for longest /
  shortest sub-array satisfying a condition.

---

## General Template (Python)

```python
def sliding_window(arr, condition):
    left = 0
    state = {}   # track window contents
    best = 0

    for right in range(len(arr)):

        # 1. Expand: add arr[right] to state
        key = arr[right]
        state[key] = state.get(key, 0) + 1

        # 2. Shrink: fix violated constraint
        while condition(state):
            remove = arr[left]
            state[remove] -= 1
            if state[remove] == 0:
                del state[remove]
            left += 1

        # 3. Update answer
        best = max(best, right - left + 1)

    return best
```

---

## Problem Types

### Max / Longest Sub-array or Sub-string
Find the longest window satisfying a constraint.

- Longest substring without repeating chars
- Longest sub-array with sum ≤ k
- Longest repeating character replacement

**Pattern:** variable window, track max length.

### Min / Shortest Sub-array or Sub-string
Find the shortest window satisfying a constraint.

- Minimum window substring
- Smallest sub-array with sum ≥ k

**Pattern:** variable window, track min length.

### Fixed-Size Window Aggregation
Compute sum, max, or average over every window
of size k.

- Maximum sum of sub-array of size k
- Sliding window maximum (monotonic deque)
- Find all anagrams in a string

**Pattern:** fixed window, slide one step at a
time.

### Count of Sub-arrays Satisfying Condition
Count sub-arrays with exactly k distinct
elements, at most k odds, etc.

**Pattern:** often solved as
`atMost(k) - atMost(k-1)`.

---

## Complexity

- **Time:** O(n) — each element enters and
  leaves the window at most once.
- **Space:** O(k) or O(alphabet) for the
  auxiliary data structure tracking window state.

---

## When to Apply Sliding Window

Ask yourself:

1. Is the input a contiguous sequence (array,
   string, linked list)?
2. Am I looking for a sub-array / sub-string?
3. Is there a constraint on the window
   (sum, distinct count, character frequency)?
4. Does the answer improve monotonically as the
   window grows (or shrinks)?

If yes to most of the above, sliding window is
likely the right approach.
