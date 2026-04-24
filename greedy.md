# Greedy Algorithms

A greedy algorithm builds a solution one step at a
time, always making the locally optimal choice at
each step and never revising a past decision.

The approach works when the problem has two
properties:

- **Greedy choice property:** a globally optimal
  solution can always be reached by making the
  locally best choice at each step.
- **Optimal substructure:** an optimal solution
  to the whole problem contains optimal solutions
  to its subproblems .

---

## Greedy vs Dynamic Programming

Both exploit optimal substructure, but they differ
in one critical way.

- **DP** explores all choices, stores subproblem
  results, and combines them to find the global
  optimum. It works even when a locally bad choice
  leads to a globally better outcome.
- **Greedy** commits to one choice per step and
  never looks back. It is faster (often O(n) or
  O(n log n)) but only correct when the greedy
  choice is provably safe.

A classic greedy failure: coin change with
denominations `[1, 3, 4]` and target `6`.
Greedy picks `4` first, leaving `1+1 = 3` coins.
DP finds `3+3 = 2` coins.

---

## Pattern 1: Scan and Accumulate

Walk the array once. At each element decide to
accumulate, reset, or skip based on a local rule.
No sorting required.

### Maximum Subarray — Kadane's Algorithm
Find the contiguous subarray with the largest sum.

- **File:** `array_hashing/maximum_subarray.py`
- **Greedy rule:** if the running sum goes negative,
  it can only hurt a future window. Reset to zero
  and start fresh from the next element.
- **Complexity:** O(n) time, O(1) space.

```python
best_sum = nums[0]
current_sum = 0
for num in nums:
    # A negative prefix shrinks every extension.
    if current_sum < 0:
        current_sum = 0
    current_sum += num
    best_sum = max(best_sum, current_sum)
return best_sum
```

**Why it is greedy:** extending a negative-sum
prefix is always wrong. No future element can
make a negative prefix worth keeping.

### Best Time to Buy and Sell Stock II
Maximize profit with unlimited buy/sell
transactions (no simultaneous holdings).

- **File:** `array_hashing/best_time_to_by_sell_stock_2.py`
- **Greedy rule:** capture every single-day price
  rise. The sum of all positive daily differences
  equals the maximum profit from any sequence of
  non-overlapping transactions.
- **Complexity:** O(n) time, O(1) space.

```python
total_profit = 0
for i in range(1, len(prices)):
    if prices[i] > prices[i - 1]:
        total_profit += prices[i] - prices[i - 1]
return total_profit
```

**Why it is greedy:** buying on day `i` and
selling on day `j` equals the sum of all positive
daily moves between `i` and `j`. Collecting each
up-day individually captures the same total.

---

## Pattern 2: Sort Then Scan

Sort the input by a carefully chosen key, then
make greedy decisions in a single left-to-right
pass. Sorting imposes an order that makes each
locally best choice globally safe.

### Non-Overlapping Intervals — Minimum Removal
Remove the fewest intervals so none overlap.

- **File:** `intervals/non-overlapping-intervals.py`
- **Greedy rule:** sort by end time; always keep
  the interval that ends earliest. It leaves the
  most room for future intervals.
- **Complexity:** O(n log n).

```python
intervals.sort(key=lambda i: i[1])
last_end = float("-inf")
kept = 0
for start, end in intervals:
    if start >= last_end:
        kept += 1
        last_end = end
return len(intervals) - kept
```

**Why sort by end?** An interval ending later
blocks more future intervals. Always committing
to the earliest end minimizes future conflicts.

### Meeting Rooms I — Overlap Detection
Determine if all meetings can be attended
(no two overlap).

- **File:** `intervals/meeting-rooms.py`
- **Greedy rule:** sort by start time; if any
  consecutive pair overlaps, attendance is
  impossible.
- **Complexity:** O(n log n).

```python
intervals.sort(key=lambda i: i.start)
for i in range(1, len(intervals)):
    if intervals[i].start < intervals[i-1].end:
        return False
return True
```

**Why sort by start?** After sorting, only
adjacent pairs can overlap. A non-adjacent pair
cannot overlap without the pair between them
also overlapping.

---

## Pattern 3: Heap-Driven Greedy

A priority queue selects the best available
element at each step. This extends the sort-then-
scan idea to problems where the "best" item
changes dynamically as elements are consumed.

### Last Stone Weight
Each turn smash the two heaviest stones together;
return the final stone weight (or 0).

- **File:** `heap_priority/last_stone_weight.py`
- **Greedy rule:** always smash the two heaviest
  first. A max-heap always surfaces the largest.
- **Complexity:** O(n log n).

```python
# Negate to use Python's min-heap as max-heap.
stones = [-s for s in stones]
heapq.heapify(stones)

while len(stones) > 1:
    first  = heapq.heappop(stones)
    second = heapq.heappop(stones)
    if first < second:
        heapq.heappush(stones, first - second)

stones.append(0)
return abs(stones[0])
```

**Why greedy works:** smashing smaller stones
first leaves a heavier stone behind and produces
a worse final result. Always eliminating the
heaviest pair is optimal.

### Task Scheduler
Find the minimum time to finish all tasks given
that the same task type must wait `n` intervals
between executions.

- **File:** `heap_priority/task_scheduler.py`
- **Greedy rule:** always run the most frequent
  remaining task. This minimizes idle time by
  filling cooldown gaps with useful work.
- **Data structures:**
  - Max-heap to pick the most frequent task.
  - Cooldown queue (deque) to hold tasks on
    cooldown with their earliest re-run time.
- **Complexity:** O(n log k) where k is the
  number of distinct task types.

```python
count = Counter(tasks)
max_heap = [-c for c in count.values()]
heapq.heapify(max_heap)
cooldown_queue = deque()
time = 0

while max_heap or cooldown_queue:
    time += 1
    if not max_heap:
        # Skip ahead to when next task is ready.
        time = cooldown_queue[0][1]
    else:
        cnt = 1 + heapq.heappop(max_heap)
        if cnt:
            cooldown_queue.append(
                [cnt, time + n]
            )
    if cooldown_queue and cooldown_queue[0][1] == time:
        heapq.heappush(
            max_heap, cooldown_queue.popleft()[0]
        )
return time
```

**Why most-frequent first?** Idle time is caused
by waiting for the most frequent task to come off
cooldown. Prioritising it keeps the CPU busy and
cannot increase the total time.

---

## Pattern 4: Greedy Graph Algorithms

Graph algorithms that commit to the cheapest
available edge or node at each step, guaranteed
correct by the cut property (MST) or by the
absence of negative weights (Dijkstra).

### Dijkstra's Algorithm — Shortest Paths
Find the shortest distance from a source node
to all other nodes in a weighted graph with
non-negative edge weights.

- **File:** `advanced_graph/network-delay-time.py`
- **Greedy rule:** always expand the unvisited
  node with the smallest known distance. Once a
  node is popped from the heap its distance is
  final.
- **Complexity:** O((V + E) log V).

```python
priority_queue = [(0, source)]
visited = set()

while priority_queue:
    dist, node = heapq.heappop(priority_queue)
    visited.add(node)
    for weight, neighbor in graph[node]:
        if neighbor not in visited:
            heapq.heappush(
                priority_queue,
                (dist + weight, neighbor),
            )
```

**Why greedy works:** with non-negative weights,
the first time a node is popped it has the true
shortest distance. A shorter path cannot arrive
later because all future paths are at least as
long.

**Why it fails with negative weights:** a later
path via a negative edge could undercut a path
already committed to. Use Bellman-Ford instead.

### Prim's Algorithm — Minimum Spanning Tree
Find the minimum cost set of edges that connects
all nodes (MST).

- **File:** `advanced_graph/min-cost-to-connect-all-points.py`
- **Greedy rule:** start from any node; always
  add the cheapest edge that connects an unvisited
  node to the growing tree.
- **Complexity:** O(E log V) with a heap.

```python
visited = set()
heap = [(0, start_node)]  # (cost, node)

while heap:
    cost, node = heapq.heappop(heap)
    if node in visited:
        continue
    visited.add(node)
    total_cost += cost
    for neighbor_cost, neighbor in graph[node]:
        if neighbor not in visited:
            heapq.heappush(
                heap, (neighbor_cost, neighbor)
            )
```

**Why greedy works — the cut property:** for any
partition of nodes into two sets, the minimum-
weight edge crossing that cut is always part of
some MST. Adding the cheapest available edge is
always safe.

**Prim vs Kruskal:** both produce an MST.
Prim grows one connected component outward using
a heap; Kruskal sorts all edges and adds them
with Union-Find. Prim is preferred on dense
graphs; Kruskal on sparse ones.

---

## Greedy Correctness: Exchange Argument

The standard proof technique for greedy algorithms
is the **exchange argument**:

1. Take any optimal solution.
2. Show that swapping a non-greedy choice for
   the greedy choice produces a solution that is
   at least as good.
3. Conclude that the greedy solution is optimal.

Example for non-overlapping intervals: suppose
an optimal solution keeps an interval `A` instead
of the greedy choice `B` (where `B` ends earlier).
Replace `A` with `B`. Since `B` ends no later than
`A`, it cannot conflict with any interval that `A`
did not conflict with. The solution is still valid
and at least as good. Therefore the greedy choice
is safe.

---

## Pattern Recognition Guide

- **Running sum / product, reset on bad prefix**
  -> Pattern 1: Kadane's (Max Subarray)

- **Collect every positive increment**
  -> Pattern 1: Stock Buy/Sell II

- **Schedule or select from sorted intervals**
  -> Pattern 2: Sort by end (keep/remove)

- **Detect conflicts in sorted events**
  -> Pattern 2: Sort by start, scan pairs

- **Repeatedly pick the globally best item**
  -> Pattern 3: Heap-driven (stones, tasks)

- **Shortest path, non-negative weights**
  -> Pattern 4: Dijkstra's algorithm

- **Minimum cost to connect all nodes**
  -> Pattern 4: Prim's or Kruskal's MST

---

## Complexity Summary

- **Scan and accumulate:** O(n) time, O(1) space.
- **Sort then scan:** O(n log n) sort dominates.
- **Heap-driven greedy:** O(n log k) where k is
  the number of distinct items in the heap.
- **Dijkstra (binary heap):** O((V+E) log V).
- **Prim (binary heap):** O(E log V).
