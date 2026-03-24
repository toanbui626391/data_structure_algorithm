# Two Pointers Algorithm

## What Is It?

The **Two Pointers** algorithm is a technique
where two indices (or "pointers") are used to
traverse a data structure, typically an array
or string.

By moving these two pointers based on specific
conditions, we can search for pairs, reverse
sequences, or eliminate redundant work, often
reducing time complexity from O(N²) to O(N).

---

## Core Idea

Instead of checking every possible combination
using nested loops, we initialize two pointers
at specific positions. We then move one or both
pointers incrementally toward a target state.

Because the pointers only move in one direction
(never backtracking completely), the entire
collection is traversed at most a few times,
guaranteeing a linear or near-linear runtime.

---

## General Implementation (Python)

There are two main patterns for two pointers.

### 1. Opposite Ends (Converging)

Used when the array is sorted, or when we are
comparing elements from the outside in (e.g.,
checking palindromes, trapping rain water).

```python
def two_pointers_converging(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        # 1. Process arr[left] and arr[right]
        # 2. Decide which pointer to move
        if condition_to_move_left:
            left += 1
        elif condition_to_move_right:
            right -= 1
        else:
            # Found exact match or target
            return [left, right]
            
    return None
```

### 2. Same Direction (Fast & Slow)

Used to detect cycles, remove duplicates, or
find the middle of a linked list. Often called
"Floyd's Tortoise and Hare".

```python
def two_pointers_same_direction(arr):
    slow = 0

    for fast in range(len(arr)):
        if condition_met(arr[fast]):
            # Move slow pointer and update
            arr[slow] = arr[fast]
            slow += 1

    return slow
```

---

## Suitable Problem Types

### Array / String Reversal or Symmetry
- **Valid Palindrome:** Check if characters at
  `left` and `right` match. Move inward.
- **Reverse String:** Swap `left` and `right`
  elements. Move inward.

### Sorted Two Sum / Pair Finding
- **Two Sum II:** If `sum > target`, decrease
  `right`. If `sum < target`, increase `left`.
- **3Sum:** Sort first, pin one number, use two
  pointers for the remaining two.

### Subsequence / Matching
- **Is Subsequence:** One pointer iterates
  through the source string, the other checks
  matches in the target sequence.

### In-Place Modifications (Fast & Slow)
- **Remove Duplicates from Sorted Array:** The
  `slow` pointer tracks the write index, `fast`
  scans for unique elements.
- **Move Zeroes:** `slow` tracks the next
  non-zero position, `fast` scans array.

### Water Trapping / Container Volumes
- **Container With Most Water:** Move the
  pointer pointing to the shorter line,
  because the shorter line limits height.
- **Trapping Rain Water:** Use `left_max` and
  `right_max` pointers moving inward.

---

## Complexity

- **Time:** O(N) or O(N log N). Traversal itself
  is strictly O(N). If the algorithm requires
  sorting first (like 3Sum), it becomes
  O(N log N) overall time.
- **Space:** O(1). Only two integer variables
  are used to track the indices.
