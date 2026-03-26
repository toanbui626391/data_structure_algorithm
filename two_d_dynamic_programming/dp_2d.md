# 2-D Dynamic Programming

2-D DP problems require two independent dimensions
to describe the state. The state is typically
written as `dp[i][j]` or memoized as `memo[(i, j)]`,
where each dimension tracks a different aspect of
the problem (e.g., index into each of two strings,
or row and column in a grid).

---

## Why Two Dimensions?

A single index is not enough when the answer at
position `i` depends on a second piece of state:

- Two strings being compared simultaneously.
- A grid coordinate `(row, col)`.
- A varying budget or capacity alongside an index.
- A buying/selling state alongside a price index.

The 2-D table stores `O(m*n)` subproblem results,
turning exponential recursion into polynomial time.

---

## Approaches

### Top-Down (Memoized DFS)
Recurse over the two indices and cache each
`(i, j)` result. Python's `@cache` or a manual
`memo` dict both work.

```python
from functools import cache

@cache
def dfs(i, j):
    # base cases
    ...
    return ...
```

### Bottom-Up (Tabulation)
Allocate a 2-D array and fill it row by row
from the base cases.

```python
dp = [[0] * (n + 1) for _ in range(m + 1)]
# fill base row / column
for i in range(1, m + 1):
    for j in range(1, n + 1):
        dp[i][j] = ...
```

---

## Pattern 1: Grid Paths

The state is a `(row, col)` coordinate. Only
forward moves are allowed (right or down), so
no visited set is needed.

### Unique Paths
Count distinct paths from the top-left to the
bottom-right of an `m x n` grid, moving only
right or down.

- **File:** `unique-paths.py`
- **Recurrence:**
  `dp[i][j] = dp[i-1][j] + dp[i][j-1]`
- **Base cases:** first row and first column
  all equal 1 (only one way to reach them).

```python
@cache
def dfs(i, j):
    if (i, j) == (m - 1, n - 1):
        return 1
    if i >= m or j >= n:
        return 0
    return dfs(i + 1, j) + dfs(i, j + 1)
```

---

## Pattern 2: Two-String DP

The state is `(i, j)` — one index into each
string. Matching characters allow a diagonal
step; mismatches require trying both strings
independently.

### Longest Common Subsequence
Find the length of the longest subsequence
present in both strings `s` and `t`.

- **File:** `longest-common-subsequence.py`
- **Recurrence (match):**
  `dp[i][j] = 1 + dp[i+1][j+1]`
- **Recurrence (no match):**
  `dp[i][j] = max(dp[i][j+1], dp[i+1][j])`

```python
@cache
def recurse(i, j):
    if i < len(s) and j < len(t):
        if s[i] == t[j]:
            return 1 + recurse(i + 1, j + 1)
        return max(
            recurse(i, j + 1),
            recurse(i + 1, j),
        )
    return 0
```

### Edit Distance
Find the minimum operations (insert, delete,
replace) to convert `word1` into `word2`.

- **File:** `edit-distance.py`
- **Recurrence (match):**
  `dp[i][j] = dp[i+1][j+1]`
- **Recurrence (no match):**
  `dp[i][j] = 1 + min(insert, delete, replace)`
  - insert  = `dp[i][j+1]`   (advance word2)
  - delete  = `dp[i+1][j]`   (advance word1)
  - replace = `dp[i+1][j+1]` (advance both)
- **Base cases:** exhausting either string costs
  the length remaining in the other.

```python
if word1[i] == word2[j]:
    answer = get_result(i + 1, j + 1)
else:
    insert  = 1 + get_result(i, j + 1)
    delete  = 1 + get_result(i + 1, j)
    replace = 1 + get_result(i + 1, j + 1)
    answer  = min(insert, delete, replace)
```

### Distinct Subsequences
Count how many distinct subsequences of `s`
equal `t`.

- **File:** `distinct-subsequences.py`
- **Recurrence:** at `(i, j)` always try
  skipping `s[i]`; if `s[i] == t[j]` also
  consume both.
- **Base cases:**
  - `j >= len(t)` -> return 1 (full match).
  - `i >= len(s)` -> return 0 (exhausted `s`).

```python
@cache
def dfs(i, j):
    if j >= len(t):
        return 1
    if i >= len(s):
        return 0
    ways = dfs(i + 1, j)         # always skip
    if s[i] == t[j]:
        ways += dfs(i + 1, j + 1)  # consume
    return ways
```

### Interleaving String
Check if `s3` is formed by interleaving `s1`
and `s2` in order.

- **File:** `interleaving-string.py`
- **State:** `(i, j)` — characters consumed
  from `s1` and `s2`. Position in `s3` is
  always `i + j`.
- **Key check:** early exit if lengths don't sum.

```python
@cache
def solve(i, j):
    if i == len(s1) and j == len(s2):
        return True
    pos = i + j
    if i < len(s1) and s3[pos] == s1[i]:
        if solve(i + 1, j):
            return True
    if j < len(s2) and s3[pos] == s2[j]:
        if solve(i, j + 1):
            return True
    return False
```

---

## Pattern 3: Pattern Matching

The second dimension indexes the pattern rather
than a plain string. Wildcard characters add
branching logic to the transitions.

### Regular Expression Matching
Match string `s` against pattern `p` where
`.` matches any single character and `*` matches
zero or more of the preceding element.

- **File:** `regular-expression-matching.py`
- **State:** `(i, j)` into `s` and `p`.
- **`*` transitions (look one ahead):**
  - Zero use: skip `c*` -> `dfs(i, j+2)`.
  - One use: current chars match -> `dfs(i+1, j)`.
- **Normal match:** advance both -> `dfs(i+1, j+1)`.

```python
same = i < len(s) and (
    s[i] == p[j] or p[j] == "."
)
if j + 1 < len(p) and p[j + 1] == "*":
    # zero-use or one-use of c*
    result = (
        dfs(i, j + 2)
        or (same and dfs(i + 1, j))
    )
else:
    result = same and dfs(i + 1, j + 1)
```

---

## Pattern 4: Counting Combinations

Two dimensions are needed when the choice of
item and the remaining capacity both matter.
Iterating over one dimension per loop keeps the
state explicit.

### Coin Change II
Count the number of combinations of coins
that sum to `amount`. Each coin may be used
unlimited times.

- **File:** `coin-change-ii.py`
- **State:** `(idx, total)` — coin index and
  current running total.
- **Transitions:**
  - Take `coins[idx]` again (stay on same coin).
  - Skip to the next coin denomination.

```python
@cache
def dfs(idx, total):
    if total == amount:
        return 1
    if total > amount or idx >= len(coins):
        return 0
    return (
        dfs(idx, total + coins[idx])
        + dfs(idx + 1, total)
    )
```

---

## Pattern 5: Assignment DP

At each element make a binary decision (+/-,
include/exclude). The second dimension tracks
the running value resulting from those choices.

### Target Sum
Assign `+` or `-` to each number; count ways
to reach `target`.

- **File:** `target-sum.py`
- **State:** `(idx, total)` — current element
  and accumulated sum so far.
- **Transitions:** add or subtract `nums[idx]`.
- **Base case:** `idx == len(nums)`, check if
  `total == target`.

```python
@cache
def dfs(idx, total):
    if idx >= len(nums):
        return 1 if total == target else 0
    return (
        dfs(idx + 1, total + nums[idx])
        + dfs(idx + 1, total - nums[idx])
    )
```

---

## Pattern 6: State Machine DP

One dimension is a positional index; the other
is a discrete mode or phase (e.g., holding vs.
not holding a stock). Transitions model valid
mode changes.

### Stock with Cooldown
Maximize profit where a one-day cooldown is
required after every sale.

- **File:**
  `best-time-to-buy-and-sell-stock-with-cooldown.py`
- **State:** `(idx, buying)` — price index and
  whether we are currently able to buy.
- **Transitions:**
  - Always: skip this day -> `dfs(idx+1, buying)`.
  - If buying: buy -> `dfs(idx+1, False) - price`.
  - If selling: sell, skip one cooldown day
    -> `dfs(idx+2, True) + price`.

```python
@cache
def dfs(idx, buying):
    if idx >= len(prices):
        return 0
    skip = dfs(idx + 1, buying)
    if buying:
        buy = dfs(idx + 1, False) - prices[idx]
        return max(skip, buy)
    else:
        sell = dfs(idx + 2, True) + prices[idx]
        return max(skip, sell)
```

---

## Pattern 7: Interval DP

The state is a range `(left, right)`. Instead
of building up from the first element, choose
the *last* element processed in a subrange.
This avoids dependency on removed elements.

### Burst Balloons
Burst all balloons to maximize coins. Bursting
balloon `i` earns `nums[i-1]*nums[i]*nums[i+1]`.

- **File:** `burst-balloons.py`
- **Key insight:** think of `i` as the *last*
  balloon burst inside `[left, right]`. The
  sentinels at `left-1` and `right+1` are still
  intact when `i` is burst.
- **Padding:** prepend and append `1` as sentinels
  so boundary math is uniform.
- **Recurrence:**
  `dp[l][r] = max over i in [l,r] of:`
  `nums[l-1]*nums[i]*nums[r+1]`
  `+ dp[l][i-1] + dp[i+1][r]`

```python
nums = [1] + nums + [1]
memo = {}

def dfs(left, right):
    if left > right:
        return 0
    if (left, right) in memo:
        return memo[(left, right)]
    best = 0
    for i in range(left, right + 1):
        coins = (
            nums[left - 1]
            * nums[i]
            * nums[right + 1]
        )
        coins += dfs(left, i - 1)
        coins += dfs(i + 1, right)
        best = max(best, coins)
    memo[(left, right)] = best
    return best
```

---

## Pattern 8: DFS with Memo on Grid

The state is `(row, col)`. Unlike shortest-path
BFS, here a cell's value strictly constrains
which neighbors are reachable, so cycles are
impossible and no visited set is needed.

### Longest Increasing Path in Matrix
Find the longest strictly increasing path in a
matrix, moving in four directions.

- **File:** `longest-increasing-path-in-a-matrix.py`
- **Key insight:** a neighbor is only visited if
  its value exceeds the current cell's value,
  guaranteeing the recursion is a DAG.
- **Answer:** run DFS from every cell; return
  `max(memo.values())`.

```python
def dfs(r, c, prev_val):
    if (
        r < 0 or r == ROWS
        or c < 0 or c == COLS
        or matrix[r][c] <= prev_val
    ):
        return 0
    if (r, c) in memo:
        return memo[(r, c)]
    val = matrix[r][c]
    best = 1 + max(
        dfs(r + 1, c, val),
        dfs(r - 1, c, val),
        dfs(r, c + 1, val),
        dfs(r, c - 1, val),
    )
    memo[(r, c)] = best
    return best
```

---

## Pattern Recognition Guide

- **Move right or down in a grid**
  -> Pattern 1: Unique Paths

- **Compare or transform two strings**
  -> Pattern 2: LCS, Edit Distance,
     Distinct Subsequences, Interleaving String

- **Match wildcards in a pattern**
  -> Pattern 3: Regex Matching

- **Count combinations with a running total**
  -> Pattern 4: Coin Change II

- **Binary decision changes a running value**
  -> Pattern 5: Target Sum

- **Mode switches (hold/sell) with constraints**
  -> Pattern 6: Stock with Cooldown

- **Subrange result independent of order**
  -> Pattern 7: Burst Balloons

- **Longest path on a grid (strictly ordered)**
  -> Pattern 8: Longest Increasing Path
