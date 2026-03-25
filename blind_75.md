# Blind 75 LeetCode Problems

A curated list of exactly 75 problems that cover the most
common patterns in technical interviews.
Organised by category to match this repository's
directory structure.

---

## Array & Hashing

- **Two Sum** — hash map for complement lookup
- **Contains Duplicate** — set membership check
- **Valid Anagram** — frequency count comparison
- **Group Anagrams** — sort key or count tuple
- **Top K Frequent Elements** — bucket sort / heap
- **Product of Array Except Self** — prefix & suffix
- **Longest Consecutive Sequence** — set + expansion
- **Encode and Decode Strings** — length-prefix scheme

---

## Two Pointers

- **Valid Palindrome** — shrink from both ends
- **3Sum** — fix one, two-pointer the rest
- **Container With Most Water** — greedy shrink

---

## Sliding Window

- **Best Time to Buy and Sell Stock** — min price tracking
- **Longest Substring Without Repeating** — char set window
- **Longest Repeating Character Replacement** — max freq
- **Minimum Window Substring** — expand + shrink

---

## Stack

- **Valid Parentheses** — matching bracket stack

---

## Binary Search

- **Find Minimum in Rotated Sorted Array** — pivot detect
- **Search in Rotated Sorted Array** — pivot + halving

---

## Linked List

- **Reverse Linked List** — iterative pointer flip
- **Merge Two Sorted Lists** — compare and link
- **Reorder List** — find mid, reverse, interleave
- **Remove Nth Node From End** — two-pointer gap
- **Linked List Cycle** — slow/fast pointer
- **Merge K Sorted Lists** — min-heap or divide/conquer

---

## Trees

- **Invert Binary Tree** — swap children recursively
- **Maximum Depth of Binary Tree** — DFS depth count
- **Same Tree** — pairwise node comparison
- **Subtree of Another Tree** — isSameTree helper
- **Lowest Common Ancestor of BST** — BST navigation
- **Binary Tree Level Order Traversal** — BFS queue
- **Validate Binary Search Tree** — min/max bounds DFS
- **Kth Smallest Element in BST** — in-order traversal
- **Binary Tree Maximum Path Sum** — post-order gain
- **Construct Tree from Preorder & Inorder** — index map
- **Serialize and Deserialize Binary Tree** — BFS encoding

---

## Trie

- **Implement Trie (Prefix Tree)** — TrieNode dict
- **Design Add and Search Words** — DFS with wildcard
- **Word Search II** — trie-guided DFS on board

---

## Heap / Priority Queue

- **Find Median From Data Stream** — two heaps (max + min)

---

## Backtracking

- **Combination Sum** — reuse elements, prune by sum
- **Word Search** — 4-directional DFS with visited

---

## Graphs

- **Number of Islands** — DFS / BFS flood fill
- **Clone Graph** — BFS + hash map of clones
- **Pacific Atlantic Water Flow** — reverse BFS
- **Course Schedule** — cycle detection
- **Graph Valid Tree** — union-find or DFS cycle check
- **Number of Connected Components** — union-find
- **Alien Dictionary** — topological sort from edges

---

## 1-D Dynamic Programming

- **Climbing Stairs** — fib recurrence
- **House Robber** — skip-adjacent max
- **House Robber II** — circular: two linear passes
- **Longest Palindromic Substring** — expand around centre
- **Palindromic Substrings** — count expansions
- **Decode Ways** — one-char and two-char steps
- **Coin Change** — bottom-up min coins
- **Maximum Product Subarray** — track min and max
- **Word Break** — reachable index DP
- **Longest Increasing Subsequence** — DP check

---

## 2-D Dynamic Programming

- **Unique Paths** — grid fill recurrence
- **Longest Common Subsequence** — 2D match table

---

## Intervals

- **Insert Interval** — find overlap, merge in place
- **Merge Intervals** — sort + extend last interval
- **Non-Overlapping Intervals** — greedy earliest end
- **Meeting Rooms** — sort + overlap check
- **Meeting Rooms II** — heap of end times

---

## Greedy

- **Maximum Subarray** — Kadane's running sum reset
- **Jump Game** — track max reachable index

---

## Bit Manipulation

- **Number of 1 Bits** — Brian Kernighan n & (n-1)
- **Counting Bits** — DP with lowest set bit
- **Reverse Bits** — shift and OR loop
- **Missing Number** — XOR with index sequence
- **Sum of Two Integers** — carry via bit ops

---

## Math & Geometry

- **Rotate Image** — transpose then mirror
- **Spiral Matrix** — shrink boundary traversal
- **Set Matrix Zeroes** — first row/col as flags
