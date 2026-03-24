# Linked List Data Structure

## What Is It?

A **Linked List** is a linear data structure
where elements, called **nodes**, are connected
by pointers.

Unlike arrays, elements are NOT stored in
contiguous memory. Each node holds:
1. **data** — the value stored.
2. **next** — a pointer to the next node.

A **Doubly Linked List** also has a `prev`
pointer pointing back to the previous node.

### Standard Node Definition (Python)
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

---

## Core Idea

The core idea is a **chain of references**.
You can only traverse the list by following
the `next` pointers from node to node
starting at the `head`.

This makes random access O(N), but insertions
and deletions anywhere in the list are O(1)
once you have a pointer to the relevant node
(no memory shifting needed unlike arrays).

---

## Common Linked List Techniques

### 1. Sentinel / Dummy Head Node

Creating a dummy node before the real `head`
simplifies edge cases like inserting at the
front or removing the head.

```python
dummy = ListNode(0)
dummy.next = head
# ...modify list...
return dummy.next
```

### 2. Fast and Slow Pointers

Two pointers at different speeds elegantly
solve many list problems without extra memory.

```python
slow = head
fast = head

while fast and fast.next:
    slow = slow.next        # moves 1 step
    fast = fast.next.next   # moves 2 steps

# When loop ends, slow is at the middle
```

### 3. Pointer Reversal

Reversing a list in-place using O(1) space.

```python
prev = None
curr = head

while curr:
    next_node = curr.next  # save next
    curr.next = prev       # reverse link
    prev = curr            # advance prev
    curr = next_node       # advance curr

return prev  # new head of reversed list
```

---

## Suitable Problem Types

### Cycle Detection
- **Linked List Cycle:** Use fast and slow
  pointers. If they meet, there is a cycle.
- **Find Cycle Start:** Once they meet, move
  one pointer to `head`. Advance both by one
  step; they will meet at the cycle's start.

### Middle / K-th Element
- **Find Middle of List:** Fast/slow approach.
  When `fast` reaches the end, `slow` is at
  the middle.
- **Kth Node from End:** Use two pointers
  separated by `k` steps. When the front
  pointer hits `None`, the back is at the
  K-th node from the end.

### Reversal
- **Reverse Linked List:** Reverse with O(1)
  space using pointer re-linking.
- **Reverse Nodes in K-Group:** Reverse each
  group of `k` nodes, reconnecting them.

### Merging and Sorting
- **Merge Two Sorted Lists:** Iterate both
  lists simultaneously, always picking the
  smaller node using a dummy head.
- **Merge K Sorted Lists:** Use a min-heap of
  size `k` to efficiently merge all lists.

### Manipulation
- **Remove N-th from End:** Two-pointer trick.
  Advance one pointer by `n` steps first.
- **Remove Duplicates from Sorted List:**
  Iterate and update `next` pointers to skip
  duplicate nodes.
- **Reorder List:** Find the middle, reverse
  the second half, then interleave the two
  halves.

---

## Complexity

- **Access (read):** O(N)
- **Search:** O(N)
- **Insertion/Deletion (at head):** O(1)
- **Insertion/Deletion (at tail or middle):**
  O(1) with a pointer, O(N) without.
- **Space:** O(N) for N nodes.
