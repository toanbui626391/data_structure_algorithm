# 1-D Dynamic Programming

Dynamic Programming (DP) solves complex problems by
breaking them into simpler subproblems and storing
results to avoid recomputation. In 1-D DP, the full
state fits in a single array `dp[i]`.

---

## Core Concepts

### Optimal Substructure
An optimal solution contains optimal solutions to
its subproblems. This lets us build the final answer
from smaller cached answers.

### Overlapping Subproblems
The same subproblem appears many times in a naive
recursion. DP stores each result once instead of
recomputing it.

---

## Approaches

### Top-Down (Memoization)
Recurse from the target downward and cache results.
Python's `@cache` decorator handles this cleanly.

```python
from functools import cache

@cache
def solve(i):
    if i <= 1:
        return i
    return solve(i - 1) + solve(i - 2)
```

### Bottom-Up (Tabulation)
Fill a `dp` array from the base cases up to the
target. No recursion stack overhead.

```python
def solve(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
```

---

## Space Optimization

When `dp[i]` depends only on `dp[i-1]` and
`dp[i-2]`, replace the full array with two rolling
variables to get O(1) space.

```python
def solve(n):
    prev2, prev1 = 0, 1
    for i in range(2, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
    return prev1
```

---

## Pattern 1: Linear Sequence

The answer at position `i` depends only on one or
two positions before it. Always space-optimizable
to O(1) with rolling variables.

### Climbing Stairs
Count distinct ways to reach step `n` taking
1 or 2 steps at a time.

- **File:** `claiming_stair.py`
- **Recurrence:** `dp[i] = dp[i-1] + dp[i-2]`
- **Base cases:** `dp[1] = 1`, `dp[2] = 2`
- **Insight:** Identical structure to Fibonacci.

```python
current, previous = 1, 1
for i in range(2, n + 1):
    current, previous = (
        current + previous,
        current,
    )
return current
```

### Min Cost Climbing Stairs
Pay `cost[i]` to leave step `i`. Minimize the
total cost to reach the top (past the last step).
You may start at step 0 or step 1.

- **File:** `min_cost_for_claiming_stairs.py`
- **Recurrence:**
  `dp[i] = cost[i] + min(dp[i-1], dp[i-2])`
- **Answer:** `min(dp[-1], dp[-2])`

```python
current, previous = 0, 0
for step_cost in cost:
    current, previous = (
        step_cost + min(current, previous),
        current,
    )
return min(current, previous)
```

---

## Pattern 2: Decision at Each Step

At each element choose to take it or skip it.
Skipping is forced when an adjacency constraint
would be violated.

### House Robber
Rob non-adjacent houses to maximize total value.

- **File:** `house_robber.py`
- **Recurrence:**
  `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`
- **Insight:** `dp[i-1]` skips house `i`;
  `dp[i-2] + nums[i]` robs it.

```python
current, previous = 0, 0
for value in nums:
    current, previous = (
        max(value + previous, current),
        current,
    )
return current
```

### House Robber II
Houses form a circle, so house 0 and house n-1
are adjacent. The linear robber cannot handle
this directly.

- **File:** `rob_house_two.py`
- **Key insight:** Either rob `nums[0..n-2]` or
  rob `nums[1..n-1]`; these two ranges cover all
  cases without including both endpoints.

```python
return max(
    rob_helper(nums[:-1]),
    rob_helper(nums[1:]),
)
```

---

## Pattern 3: Unbounded Knapsack

Each item can be used any number of times.
Iterate forward over capacities so the same item
can be reused freely within one pass.

### Coin Change
Find the minimum number of coins to sum to
`amount`.

- **File:** `coin_change.py`
- **Recurrence:**
  `dp[a] = min(dp[a], dp[a - coin] + 1)`
- **Base case:** `dp[0] = 0`
- **Init:** fill with `inf`; return -1 if
  `dp[amount]` stays `inf`.

```python
dp = [float("inf")] * (amount + 1)
dp[0] = 0
for coin in coins:
    for target in range(coin, amount + 1):
        dp[target] = min(
            dp[target],
            dp[target - coin] + 1,
        )
```

---

## Pattern 4: String Segmentation

`dp[i]` represents whether the first `i`
characters satisfy a condition. For each endpoint
scan all split points to combine valid left and
right parts.

### Decode Ways
Count ways to decode a digit string into letters
where A=1 ... Z=26.

- **File:** `decode_ways.py`
- **Approach:** Top-down with `@cache`.
- **Transitions:**
  - Decode one char if `s[i]` is `'1'`-`'9'`.
  - Decode two chars if `s[i:i+2]` is `10`-`26`.
- **Base case:** empty string returns 1.

```python
@cache
def dfs(sub):
    if not sub:
        return 1
    one = 0
    two = 0
    if 1 <= int(sub[:1]) <= 9:
        one = dfs(sub[1:])
    if len(sub) >= 2 and 10 <= int(sub[:2]) <= 26:
        two = dfs(sub[2:])
    return one + two
```

### Word Break
Check if a string can be segmented into words
from a dictionary.

- **File:** `wordbreak.py`
- **Recurrence:** `dp[end] = True` if there
  exists `start` where `dp[start]` is True
  and `s[start:end]` is in the dictionary.
- **Base case:** `dp[0] = True` (empty prefix).

```python
dp = [True] + [False] * len(s)
for end in range(1, len(s) + 1):
    for start in range(end + 1):
        if dp[start] and s[start:end] in wordDict:
            dp[end] = True
```

---

## Pattern 5: Subsequence and Substring

### Longest Increasing Subsequence
Find the length of the longest strictly increasing
subsequence (LIS).

- **File:** `longest_increasing_subsequence.py`
- **Recurrence:** for each `j < i` where
  `nums[j] < nums[i]`:
  `dp[i] = max(dp[i], dp[j] + 1)`
- **Init:** `dp[i] = 1` (each element is a
  length-1 subsequence on its own).
- **Answer:** `max(dp)`
- **Complexity:** O(n²) time, O(n) space.

```python
dp = [1] * len(nums)
for i in range(len(nums)):
    for pos in range(i):
        if nums[pos] < nums[i]:
            dp[i] = max(dp[i], dp[pos] + 1)
return max(dp)
```

### Longest Palindromic Substring
Find the longest palindromic substring.

- **File:** `longest_palindrome_substring.py`
- **Approach:** Expand-around-center.
  O(n²) time, O(1) space — no DP array needed.
- **Two center types:**
  - Odd-length: single center at index `i`.
  - Even-length: gap between `i` and `i+1`.

```python
best = ''
for i in range(len(s)):
    odd  = expand(s, i, i)
    even = expand(s, i, i + 1)
    best = max([best, odd, even], key=len)
```

---

## Pattern 6: Running Min and Max

Track both the running minimum and maximum
because a negative number can flip the worst
product into the best on the next step.

### Max Product Subarray
Find the contiguous subarray with the largest
product.

- **File:** `max_product_subarray.py`
- **Key insight:** Negative × negative = positive,
  so `cur_min` must be maintained alongside
  `cur_max` at every step.
- **Recurrence at each value:**
  `candidates = (value, value*cur_min, value*cur_max)`
  `cur_min = min(candidates)`
  `cur_max = max(candidates)`

```python
cur_min = cur_max = 1
result = nums[0]
for value in nums:
    cands = (
        value,
        value * cur_min,
        value * cur_max,
    )
    cur_min = min(cands)
    cur_max = max(cands)
    result = max(result, cur_max)
```

---

## Pattern 7: 0/1 Knapsack

Each item may be used at most once. Iterate
backward over capacities so no item is counted
twice in the same pass.

### Partition Equal Subset
Check if the array can be split into two subsets
with equal sum.

- **File:** `partition_equal_subset.py`
- **Reduction:** Find a subset summing to
  `total // 2` (impossible when total is odd).
- **Recurrence:**
  `dp[curr] = dp[curr] or dp[curr - num]`
- **Backward sweep:** prevents reusing the same
  number more than once per pass.

```python
dp = [True] + [False] * half
for num in nums:
    for curr in range(half, num - 1, -1):
        dp[curr] = dp[curr] or dp[curr - num]
return dp[-1]
```

---

## Pattern Recognition Guide

- **Fibonacci-like, no adjacency constraint**
  -> Pattern 1: Climbing Stairs
- **Take or skip, adjacency forbidden**
  -> Pattern 2: House Robber
- **Items unlimited, reach a target sum**
  -> Pattern 3: Coin Change
- **Segment a string by rules or dictionary**
  -> Pattern 4: Decode Ways, Word Break
- **Longest valid subsequence or substring**
  -> Pattern 5: LIS, Palindrome
- **Product with sign-flip risk**
  -> Pattern 6: Max Product Subarray
- **Subset with target sum, each item once**
  -> Pattern 7: Partition Equal Subset
