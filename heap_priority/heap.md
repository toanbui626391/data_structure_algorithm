# Heap Data Structure

## What is a Heap?
A heap is a specialized tree-based data structure that
satisfies the "heap property". It is almost always
implemented as a complete binary tree. 

There are two main types of heaps:
* **Max-Heap:** The value of each node is greater than
  or equal to the values of its children. The largest
  value in the heap is stored at the root.
* **Min-Heap:** The value of each node is less than or
  equal to the values of its children. The smallest
  value in the heap is stored at the root.

## Core Idea of a Heap
The core idea is to maintain partial order. Unlike
a binary search tree (which keeps all elements perfectly
sorted), a heap only guarantees that the parent is
"better" (smaller or larger) than its children.

This partial sorting makes it extremely efficient for:
* Finding the min/max element in O(1) time.
* Inserting a new element in O(log n) time.
* Removing the min/max element in O(log n) time.

Because it is a complete binary tree, it can be efficiently
represented as a simple array, avoiding the overhead of
pointers used in standard trees.

## What Problems are Solved by a Min-Heap?
A min-heap is your go-to data structure whenever a problem
asks you to constantly access the **smallest** items from a
dynamic collection. 

Common problem patterns include:

* **Top K Elements:** Finding the K largest or smallest
  elements in a stream or an array.
* **Merging K Sorted Lists:** Combining multiple sorted
  lists into one. The heap keeps track of the current
  minimum across all lists.
* **Dijkstra's Algorithm:** Finding the shortest path in
  a graph. A min-heap easily tracks the nearest unvisited
  node.
* **Task Scheduling:** When tasks have priorities or finish
  times, a heap efficiently grabs the next task to run.
* **Median of a Data Stream:** Combining a max-heap and
  min-heap is the optimal way to track the median value
  as new data arrives.

## Python Implementation
Python provides the `heapq` module, which implements a
min-heap using standard lists.

```python
import heapq

# Initializing
min_heap = []

# Pushing elements (O(log n))
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 2)
heapq.heappush(min_heap, 8)

# Popping the smallest element (O(log n))
smallest = heapq.heappop(min_heap) # Returns 2

# Accessing smallest without popping (O(1))
peek = min_heap[0] # Returns 5
```
