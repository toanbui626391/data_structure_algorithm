# Intervals

An interval represents a contiguous range on a
number line, written as `[start, end]`. Interval
problems ask you to reason about how ranges relate
to each other: do they overlap, can they be merged,
how many are active at once?

---

## Core Definitions

### Overlap
Two intervals `[a, b]` and `[c, d]` overlap when
one starts before the other ends.

```
overlap  when: a <= d  AND  c <= b
no overlap when: b < c  OR  d < a
```

Equivalently, two intervals do NOT overlap when one
ends strictly before the other begins.

### Containment
`[c, d]` is contained inside `[a, b]` when
`a <= c` and `d <= b`.

### Adjacency
`[a, b]` and `[b, c]` are adjacent (touching at
a single point). Depending on the problem they
may be treated as overlapping or non-overlapping.

---

## Fundamental Techniques

### Sort by Start Time
Most interval algorithms begin by sorting on the
start coordinate. This turns a 2-D comparison into
a single left-to-right sweep.

```python
intervals.sort(key=lambda itv: itv[0])
```

After sorting, any interval that does not overlap
the current one also cannot overlap any earlier
interval. This property drives greedy solutions.

### Linear Sweep
Walk through sorted intervals left to right,
maintaining a "current" merged interval. When
the next interval overlaps, extend the current
end; otherwise, emit the current interval and
advance.

```python
last = intervals[0]
for curr in intervals[1:]:
    if curr[0] <= last[1]:
        # Extend to cover both.
        last[1] = max(last[1], curr[1])
    else:
        result.append(last)
        last = curr
result.append(last)
```

**Overlap condition after sorting:** `curr[0] <= last[1]`
Because intervals are sorted by start, we only
need to compare the new start against the last
merged end.

### Min-Heap of End Times
To track how many intervals are active at any
moment, push each interval's end time onto a
min-heap. Before adding a new interval, pop all
entries whose end time is <= the new start time
(those rooms/resources are free).

```python
import heapq
end_heap = []
for start, end in sorted_intervals:
    # Release finished intervals.
    while end_heap and end_heap[0] <= start:
        heapq.heappop(end_heap)
    heapq.heappush(end_heap, end)
# Heap size = active intervals right now.
```

**Why a min-heap?** We always want to reuse the
room that finishes earliest. A min-heap gives the
smallest end time in O(log n).

### Greedy: Keep the Earliest-Ending Interval
When choosing which intervals to keep (or remove)
to eliminate overlap, always prefer the interval
with the smaller end time. A smaller end leaves
more room for future intervals.

This is the interval scheduling maximization
greedy: sort by end time, keep an interval if it
does not overlap the last kept one.

### Three-Region Partition (Insert)
When inserting a new interval into a sorted list,
every existing interval falls into exactly one of
three regions:

- **Before:** ends before the new interval starts.
  Append as-is.
- **Overlap:** overlaps the new interval.
  Merge into the new interval by expanding its
  bounds.
- **After:** starts after the new interval ends.
  Append as-is after flushing the merged result.

---

## Problems

### Meeting Rooms I — Overlap Detection
Determine if a person can attend all meetings
(no two intervals may overlap).

- **File:** `meeting-rooms.py`
- **Algorithm:** Sort by start; check every
  consecutive pair for overlap.
- **Overlap check:** `intervals[i].start < intervals[i-1].end`
- **Complexity:** O(n log n) sort, O(n) scan.

```python
intervals.sort(key=lambda i: i.start)
for i in range(1, len(intervals)):
    if intervals[i].start < intervals[i-1].end:
        return False
return True
```

**Key insight:** After sorting, only consecutive
pairs need to be checked. A non-consecutive pair
cannot overlap if the pair between them does not.

---

### Merge Intervals — Merge Overlapping
Collapse all overlapping intervals into the
fewest non-overlapping intervals.

- **File:** `merge-intervals.py`
- **Algorithm:** Sort by start; linear sweep
  extending the last interval's end on overlap.
- **Complexity:** O(n log n).

```python
intervals.sort()
last = intervals[0]
for curr in intervals[1:]:
    if curr[0] <= last[1]:
        last[1] = max(last[1], curr[1])
    else:
        merged.append(last)
        last = curr
merged.append(last)
```

**Key insight:** After sorting, `curr[0] <= last[1]`
is the only condition needed. We never need to
look further back than the last merged interval.

---

### Insert Interval — Insert and Merge
Insert a new interval into a sorted, non-
overlapping list and merge any resulting overlaps.

- **File:** `insert-interval.py`
- **Algorithm:** Three-region single pass.
  No sort needed because input is already sorted.
- **Complexity:** O(n).

```python
for interval in intervals:
    # Region 1: interval ends before new starts.
    if interval[1] < new_interval[0]:
        result.append(interval)
    # Region 3: interval starts after new ends.
    elif interval[0] > new_interval[1]:
        result.append(new_interval)
        new_interval = interval
    # Region 2: overlap — expand new interval.
    else:
        new_interval[0] = min(
            interval[0], new_interval[0]
        )
        new_interval[1] = max(
            interval[1], new_interval[1]
        )
result.append(new_interval)
```

**Key insight:** Treat `new_interval` as a
rolling accumulator. It absorbs every overlapping
interval and is flushed when a gap is found.

---

### Meeting Rooms II — Resource Counting
Find the minimum number of conference rooms
needed to host all meetings simultaneously.

- **File:** `meeting-rooms-ii.py`
- **Algorithm:** Sort by start; use a min-heap
  of end times to simulate room allocation.
- **Complexity:** O(n log n).

```python
sorted_meetings = sorted(intervals,
                         key=lambda i: i.start)
end_heap = []
for interval in sorted_meetings:
    start, end = interval.start, interval.end
    # Free rooms that ended before this starts.
    while end_heap and end_heap[0] <= start:
        heapq.heappop(end_heap)
    heapq.heappush(end_heap, end)
    result = max(result, len(end_heap))
```

**Key insight:** The heap size at any point equals
the number of overlapping meetings. We always
reuse the room finishing soonest, which is why
a min-heap (not max-heap) is correct.

---

### Non-Overlapping Intervals — Minimum Removal
Find the minimum number of intervals to remove
so that no two intervals overlap.

- **File:** `non-overlapping-intervals.py`
- **Algorithm:** Sort by start; memoized DP
  finds the longest non-overlapping chain; the
  answer is total minus that chain length.
- **Complexity:** O(n²) DP, O(n log n) sort.

```python
intervals.sort()

@cache
def dp(idx):
    start, end = intervals[idx]
    for pos in range(idx + 1, len(intervals)):
        next_start, next_end = intervals[pos]
        if end <= next_start:
            # No overlap: extend chain.
            return 1 + dp(pos)
        if end > next_end:
            # Contained: skip contained interval.
            return dp(pos)
    return 1

removals = len(intervals) - dp(0)
```

**Greedy alternative:** Sort by end time; greedily
keep each interval that does not overlap the last
kept one. This runs in O(n log n) and is simpler.

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

---

### Minimum Interval for Each Query
For each query point, find the size of the
smallest interval that contains it. Return -1
if no interval covers the query.

- **File:** `minimum-interval-to-include-each-query.py`
- **Algorithm:** Sort intervals by start and
  queries by value. Sweep queries left to right;
  push intervals whose start <= query onto a
  min-heap keyed by size `(end-start+1, end)`.
  Pop intervals whose end < query (no longer
  cover it). The heap top is the answer.
- **Complexity:** O((n+q) log n).

```python
intervals.sort()
sorted_queries = sorted(
    enumerate(queries), key=lambda x: x[1]
)
answers = [-1] * len(queries)
heap = []   # (size, end)
idx = 0
for orig_idx, q in sorted_queries:
    # Push all intervals starting at or before q.
    while idx < len(intervals):
        start, end = intervals[idx]
        if start > q:
            break
        heapq.heappush(heap, (end-start+1, end))
        idx += 1
    # Pop intervals that no longer cover q.
    while heap and heap[0][1] < q:
        heapq.heappop(heap)
    if heap:
        answers[orig_idx] = heap[0][0]
```

**Key insight:** Sort both intervals and queries
so intervals are pushed lazily. Popping by end
time keeps only the intervals still covering the
current query. The smallest remaining is on top.

---

## Algorithm Selection Guide

- **Do any two intervals overlap?**
  -> Sort by start; scan consecutive pairs.

- **Collapse all overlaps into fewer intervals**
  -> Sort by start; linear sweep with merge.

- **Insert one new interval into a sorted list**
  -> Three-region single pass; no re-sort needed.

- **How many intervals are active at the same time?**
  -> Sort by start; min-heap of end times.

- **Remove the fewest intervals to eliminate all overlaps**
  -> Sort by end; greedy keep-earliest-ending.

- **For each query, find the best covering interval**
  -> Sort both; sweep with a min-heap keyed by
  the metric you want to minimize (size, end, etc).

---

## Complexity Summary

- **Sort by start:** O(n log n) — required by
  almost every interval algorithm.
- **Linear sweep (merge/insert):** O(n) after sort.
- **Min-heap sweep:** O(n log n) total — each
  interval is pushed and popped at most once.
- **Greedy keep chain:** O(n) after sort.
- **DP longest chain:** O(n²) — use greedy when
  possible.
