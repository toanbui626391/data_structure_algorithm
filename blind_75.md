# Blind 75 LeetCode Problems

A curated list of 75 problems that cover the most
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
- **Valid Sudoku** — row / col / box sets

---

## Two Pointers

- **Valid Palindrome** — shrink from both ends
- **Two Sum II (sorted input)** — left + right pointer
- **3Sum** — fix one, two-pointer the rest
- **Container With Most Water** — greedy shrink
- **Trapping Rain Water** — left/right max arrays

---

## Sliding Window

- **Best Time to Buy and Sell Stock** — min price
  tracking (single pass)
- **Longest Substring Without Repeating** — char set
  window
- **Longest Repeating Character Replacement** — max
  freq in window
- **Permutation in String** — fixed-size window count
- **Minimum Window Substring** — expand + shrink
- **Sliding Window Maximum** — monotonic deque

---

## Stack

- **Valid Parentheses** — matching bracket stack
- **Min Stack** — auxiliary min stack
- **Evaluate Reverse Polish Notation** — operand stack
- **Generate Parentheses** — backtrack with counts
- **Daily Temperatures** — monotonic decreasing stack
- **Car Fleet** — stack of arrival times
- **Largest Rectangle in Histogram** — monotonic stack

---

## Binary Search

- **Binary Search** — classic halving
- **Search a 2D Matrix** — flatten index mapping
- **Koko Eating Bananas** — binary search on answer
- **Find Minimum in Rotated Sorted Array** — pivot
  detection
- **Search in Rotated Sorted Array** — pivot + halving
- **Time Based Key-Value Store** — binary search on
  timestamps
- **Median of Two Sorted Arrays** — binary search on
  partition

---

## Linked List

- **Reverse Linked List** — iterative pointer flip
- **Merge Two Sorted Lists** — compare and link
- **Reorder List** — find mid, reverse, interleave
- **Remove Nth Node From End** — two-pointer gap
- **Linked List Cycle** — slow/fast pointer
- **Merge K Sorted Lists** — min-heap or divide/conquer
- **Copy List With Random Pointer** — hash map clone
- **Find the Duplicate Number** — Floyd's cycle
  detection
- **Add Two Numbers** — digit-by-digit with carry
- **Reverse Nodes in K-Group** — reverse in chunks

---

## Trees

- **Invert Binary Tree** — swap children recursively
- **Maximum Depth of Binary Tree** — DFS depth count
- **Diameter of Binary Tree** — max left + right depth
- **Balanced Binary Tree** — height check at each node
- **Same Tree** — pairwise node comparison
- **Subtree of Another Tree** — isSameTree helper
- **Lowest Common Ancestor of BST** — BST property
  navigation
- **Binary Tree Level Order Traversal** — BFS queue
- **Binary Tree Right Side View** — last node per level
- **Count Good Nodes in Binary Tree** — path max DFS
- **Validate Binary Search Tree** — min/max bounds DFS
- **Kth Smallest Element in BST** — in-order traversal
- **Binary Tree Maximum Path Sum** — post-order gain
- **Construct Tree from Preorder & Inorder** — index
  map recursion
- **Serialize and Deserialize Binary Tree** — BFS
  level encoding

---

## Trie

- **Implement Trie (Prefix Tree)** — TrieNode children
  dict
- **Design Add and Search Words** — DFS with wildcard
- **Word Search II** — trie-guided DFS on board

---

## Heap / Priority Queue

- **Kth Largest Element in Array** — min-heap of size k
- **Kth Largest Element in Stream** — live min-heap
- **K Closest Points to Origin** — max-heap of size k
- **Last Stone Weight** — max-heap simulation
- **Task Scheduler** — greedy with frequency heap
- **Design Twitter** — per-user heaps merged
- **Find Median From Data Stream** — two heaps
  (max + min)

---

## Backtracking

- **Subsets** — include / exclude at each step
- **Subsets II** — skip duplicates after sorting
- **Combination Sum** — reuse elements, prune by sum
- **Combination Sum II** — no reuse, skip duplicates
- **Permutations** — swap or used-flag DFS
- **Word Search** — 4-directional DFS with visited
- **Palindrome Partitioning** — cut + check palindrome
- **Letter Combinations of Phone Number** — digit map
  DFS
- **N-Queens** — col + diagonal set constraints

---

## Graphs

- **Number of Islands** — DFS / BFS flood fill
- **Max Area of Island** — flood fill with area count
- **Clone Graph** — BFS + hash map of clones
- **Walls and Gates** — multi-source BFS
- **Rotting Oranges** — multi-source BFS with timer
- **Pacific Atlantic Water Flow** — reverse BFS from
  each ocean
- **Surrounded Regions** — border DFS to mark safe
- **Course Schedule** — cycle detection (DFS / Kahn)
- **Course Schedule II** — topological order output
- **Graph Valid Tree** — union-find or DFS cycle check
- **Number of Connected Components** — union-find
- **Redundant Connection** — union-find, return edge
- **Word Ladder** — BFS with one-char mutations

---

## Advanced Graphs

- **Reconstruct Itinerary** — Hierholzer (Eulerian
  path)
- **Min Cost to Connect All Points** — Prim's MST
- **Network Delay Time** — Dijkstra single source
- **Swim in Rising Water** — Dijkstra / binary search
- **Alien Dictionary** — topological sort from edges
- **Cheapest Flights Within K Stops** — Bellman-Ford
  limited iterations

---

## 1-D Dynamic Programming

- **Climbing Stairs** — fib recurrence
- **Min Cost Climbing Stairs** — cost + prev two
- **House Robber** — skip-adjacent max
- **House Robber II** — circular: two linear passes
- **Longest Palindromic Substring** — expand around
  centre
- **Palindromic Substrings** — count expansions
- **Decode Ways** — one-char and two-char steps
- **Coin Change** — bottom-up min coins
- **Maximum Product Subarray** — track min and max
- **Word Break** — reachable index DP
- **Longest Increasing Subsequence** — patience sort /
  DP
- **Partition Equal Subset Sum** — 0/1 knapsack bool

---

## 2-D Dynamic Programming

- **Unique Paths** — grid fill recurrence
- **Longest Common Subsequence** — 2D match table
- **Best Time to Buy/Sell Stock with Cooldown** — state
  machine DP
- **Coin Change II** — unbounded knapsack count
- **Target Sum** — DP over sum range
- **Interleaving String** — 2D string merge DP
- **Longest Increasing Path in Matrix** — memoised DFS
- **Distinct Subsequences** — 2D count table
- **Edit Distance** — insert/delete/replace DP
- **Burst Balloons** — interval DP
- **Regular Expression Matching** — 2D state DP

---

## Intervals

- **Insert Interval** — find overlap, merge in place
- **Merge Intervals** — sort + extend last interval
- **Non-Overlapping Intervals** — greedy earliest end
- **Meeting Rooms** — sort + overlap check
- **Meeting Rooms II** — heap of end times
- **Minimum Interval to Include Each Query** — sort +
  min-heap sweep

---

## Greedy

- **Maximum Subarray** — Kadane's running sum reset
- **Jump Game** — track max reachable index
- **Jump Game II** — greedy level BFS
- **Gas Station** — total surplus check + start reset
- **Hand of Straights** — greedy group formation
- **Merge Triplets to Form Target** — valid triplet
  filter
- **Partition Labels** — last occurrence map
- **Valid Parenthesis String** — greedy min/max open

---

## Bit Manipulation

- **Single Number** — XOR all elements
- **Number of 1 Bits** — Brian Kernighan n & (n-1)
- **Counting Bits** — DP with lowest set bit
- **Reverse Bits** — shift and OR loop
- **Missing Number** — XOR with index sequence
- **Sum of Two Integers** — carry via bit ops
- **Reverse Integer** — digit extraction loop

---

## Math & Geometry

- **Rotate Image** — transpose then mirror
- **Spiral Matrix** — shrink boundary traversal
- **Set Matrix Zeroes** — first row/col as flags
- **Happy Number** — digit square sum cycle detect
- **Plus One** — carry propagation
- **Pow(x, n)** — fast exponentiation (halving)
- **Multiply Strings** — grade-school digit multiply
- **Detect Squares** — frequency map geometry
