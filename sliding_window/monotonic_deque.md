# Monotonic Deque

## What Is a Monotonic Deque?

A **monotonic deque** is a double-ended queue
(deque) where the elements are kept strictly in
increasing or decreasing order.

- **Monotonically Increasing:** Elements from
  front to back only increase (or stay equal).
- **Monotonically Decreasing:** Elements from
  front to back only decrease (or stay equal).

When a new element arrives, we pop elements
from the back of the deque that violate the
chosen monotonic property before pushing the
new element.

---

## Why Is It Classified as Sliding Window?

A monotonic deque is the optimal data structure
for finding the **maximum or minimum in a
sliding window**.

When a window slides over an array:
1. **New elements enter** the window.
2. **Old elements exit** the window.

A monotonic deque helps us keep track of the
"best" or "most extreme" values in the current
window without having to re-scan all the elements.
It acts as a smart memory for the sliding window
by discarding values that are structurally useless.

---

## Why Do We Discard Elements?

Consider finding the **maximum** in a sliding
window. We use a **monotonically decreasing
deque**.

Imagine a window with elements `[3, 1, 4]`.
When `4` enters the window, both `3` and `1`
become completely irrelevant. Why?
1. `4` is larger than them.
2. `4` entered *after* them, so it will survive
   in the window *longer* than they will.

Thus, any element smaller than the incoming
element is popped from the back. The front of the
deque will always hold the maximum value for the
current window.

---

## Operations in a Sliding Window

For each element as the window slides:

1. **Pop from Back (Maintain Order):**
   While the deque is not empty and the current
   element is "better" than the element at the
   back, pop the back element.
2. **Push to Back:**
   Add the current element (or its index) to the
   back of the deque.
3. **Pop from Front (Maintain Window Size):**
   If the element at the front of the deque has
   fallen outside the left boundary of the window,
   pop it from the front.
4. **Get Answer:**
   The element at the front is the answer (min
   or max) for the current window.

---

## Common Problem Patterns

A monotonic deque is primarily used when you
need O(1) retrieval of the max/min over a dynamic
range and O(N) overall time complexity.

### 1. Sliding Window Maximum / Minimum
- **Problem:** Given an array and window size `k`,
  find the max/min in every window.
- **Why Deque:** A naive scan takes O(n*k). A
  max-heap takes O(n log k). A monotonic deque
  takes O(n) because each element is pushed and
  popped exactly once.

### 2. Next Greater / Smaller Element
- **Problem:** Find the first element to the
  right that is strictly greater or smaller.
- **Why Deque:** As you scan, you keep a stack of
  unresolved elements. (In this case, a deque
  used as a stack).

### 3. Longest Sub-array with Absolute Limits
- **Problem:** Find longest sub-array where the
  absolute difference between max and min is ≤ k.
- **Why Deque:** Use two monotonic deques—one
  for the max, one for the min—to track the
  extremes as the variable window expands.

---

## Complexity

- **Time:** O(N) — Every element is pushed at most
  once and popped at most once.
- **Space:** O(K) — Where K is the size of the
  window, because the deque only stores elements
  currently inside the window.
