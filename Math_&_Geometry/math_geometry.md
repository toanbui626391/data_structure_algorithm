# Math and Geometry

Math and geometry problems rely on numerical
properties, spatial reasoning, and in-place
manipulation rather than on classic data
structures. Most solutions are O(1) space and
hinge on one clean mathematical insight.

---

## Core Mathematical Tools

### Digit Extraction
Extract digits from an integer one at a time
using modulo and floor division.

```python
while n > 0:
    digit = n % 10    # rightmost digit
    n = n // 10       # drop that digit
```

Build an integer from digits in reverse by
multiplying the accumulator by 10 each step.

```python
result = 0
for digit in digits:
    result = result * 10 + digit
```

### Carry Propagation
When adding 1 to a digit, a carry occurs when
that digit is 9. Reset to 0 and propagate left.
If the loop exhausts without returning, all
digits were 9; prepend a leading 1.

```python
for i in range(len(digits) - 1, -1, -1):
    if digits[i] < 9:
        digits[i] += 1
        return digits
    digits[i] = 0
return [1] + digits
```

### Fast Exponentiation (Halving)
Compute `x^n` in O(log n) by halving the
exponent at each step.

```
x^n = (x^(n/2))^2        when n is even
x^n = x * x^(n-1)        when n is odd
x^n = 1 / x^(-n)         when n is negative
```

Each halving step halves the remaining work,
giving O(log n) recursive calls.

### Cycle Detection via Visited Set
Some sequences are guaranteed to either reach
a fixed point or loop. Track visited values
in a set; a repeat means a cycle.

```python
visited = set()
while n != 1:
    if n in visited:
        return False   # cycle detected
    visited.add(n)
    n = next_value(n)
return True
```

---

## Pattern 1: In-Place Matrix Transformation

Manipulate a 2-D array without extra space.
The key is understanding how indices transform
under the operation, then applying the
transformation layer by layer or cell by cell.

### Rotate Image
Rotate an n x n matrix 90 degrees clockwise
in place.

- **File:** `rotate-image.py`
- **Two-step decomposition:**
  - Step 1 — transpose: swap `matrix[i][j]`
    with `matrix[j][i]` across the diagonal.
  - Step 2 — reverse each row left-to-right.
- **Why it works:**
  A 90° clockwise rotation maps
  `(row, col)` -> `(col, n-1-row)`.
  Transposing maps `(row, col)` -> `(col, row)`.
  Reversing rows maps `col` -> `n-1-col`.
  Chaining gives `(col, n-1-row)` — exactly
  a 90° clockwise rotation.
- **Complexity:** O(n²) time, O(1) space.

```python
# Step 1: transpose (upper triangle only).
for i in range(n):
    for j in range(i, n):
        matrix[i][j], matrix[j][i] = (
            matrix[j][i], matrix[i][j]
        )

# Step 2: reverse each row.
for row in matrix:
    left, right = 0, n - 1
    while left < right:
        row[left], row[right] = (
            row[right], row[left]
        )
        left += 1
        right -= 1
```

**Rotation variants:**
- 90° counter-clockwise: transpose then
  reverse each column (or reverse rows first,
  then transpose).
- 180°: reverse the entire matrix top-to-bottom,
  then reverse each row.

---

### Spiral Matrix
Return all matrix elements in clockwise spiral
order.

- **File:** `spiral-matrix.py`
- **Technique:** shrinking-boundary traversal.
  Maintain four pointers `top`, `bottom`,
  `left`, `right`. Each full loop traverses
  one layer and tightens the boundary.
- **Four traversal directions per layer:**
  - Left -> right along `top`; then `top += 1`
  - Top -> bottom along `right`; then `right -= 1`
  - Right -> left along `bottom`; then `bottom -= 1`
  - Bottom -> top along `left`; then `left += 1`
- **Trim:** slice result to `m * n` elements to
  discard duplicates on odd-sized matrices.
- **Complexity:** O(m*n) time, O(1) extra space.

```python
while left <= right and top <= bottom:
    for c in range(left, right + 1):
        result.append(matrix[top][c])
    top += 1

    for r in range(top, bottom + 1):
        result.append(matrix[r][right])
    right -= 1

    for c in range(right, left - 1, -1):
        result.append(matrix[bottom][c])
    bottom -= 1

    for r in range(bottom, top - 1, -1):
        result.append(matrix[r][left])
    left += 1

return result[:m * n]
```

---

### Set Matrix Zeroes
If any cell is 0, set its entire row and
column to 0, in place.

- **File:** `set-matrix-zeroes.py`
- **Two-pass approach:**
  - Pass 1: collect the row and column indices
    of every zero cell into two sets.
  - Pass 2: zero out all collected rows, then
    all collected columns.
- **Why two passes?** Setting zeros during the
  first pass would corrupt the zero-detection
  logic for cells not yet visited.
- **Complexity:** O(m*n) time, O(m+n) space
  for the index sets.

```python
zero_rows, zero_cols = set(), set()

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == 0:
            zero_rows.add(i)
            zero_cols.add(j)

for r in zero_rows:
    for j in range(cols):
        matrix[r][j] = 0

for c in zero_cols:
    for i in range(rows):
        matrix[i][c] = 0
```

**O(1) space variant:** use the first row and
first column themselves as flag arrays, saving
whether they originally contained a zero with
two boolean variables before overwriting them.

---

## Pattern 2: Digit-by-Digit Arithmetic

Simulate pencil-and-paper arithmetic by
processing one digit at a time. All problems
in this pattern avoid Python's big-integer
`int()` by building values manually.

### Plus One
Increment a large integer stored as a digit
array.

- **File:** `plus-one.py`
- **Technique:** right-to-left carry propagation.
  A digit less than 9 absorbs the increment
  and stops. A 9 becomes 0 and passes the
  carry left. If the loop completes, prepend 1.
- **Complexity:** O(n) worst case (all 9s),
  O(1) average.

```python
for i in range(len(digits) - 1, -1, -1):
    if digits[i] < 9:
        digits[i] += 1
        return digits
    digits[i] = 0
return [1] + digits
```

---

### Multiply Strings
Multiply two non-negative integers given as
strings without using `int()`.

- **File:** `multiply-strings.py`
- **Technique:** parse each string into an
  integer digit by digit using `ord(c) - ord('0')`
  to convert a character to its numeric value,
  then multiply the two parsed values.
- **Complexity:** O(m + n) to parse,
  O(1) for the multiply.

```python
def _parse(num_str):
    result = 0
    for ch in num_str:
        result = result * 10 + ord(ch) - ord('0')
    return result

return str(_parse(num1) * _parse(num2))
```

**Full grade-school variant** (when `int()`
is truly forbidden): allocate a result array
of length `m + n`, multiply each digit pair,
accumulate at the correct position, then
convert digits back to a string.

---

## Pattern 3: Fast Exponentiation

### Pow(x, n)
Compute x raised to the power n, including
negative n and n = 0.

- **File:** `powx-n.py`
- **Technique:** recursive halving.
  - `n == 0`: return 1 (base case).
  - `n < 0`: invert and recurse on `|n|`.
  - `n` even: `myPow(x, n//2)²`.
  - `n` odd: `x * myPow(x, n-1)`.
- **Complexity:** O(log n) time, O(log n)
  stack space.

```python
def myPow(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / (x * myPow(x, -n - 1))
    if n % 2 == 0:
        half = myPow(x, n // 2)
        return half * half
    return x * myPow(x, n - 1)
```

**Why `1 / (x * myPow(x, -n-1))` and not
`1 / myPow(x, -n)`?** When `n` is `INT_MIN`
(`-2^31`), `-n` overflows in languages with
fixed-width integers. Writing `-n - 1` shifts
to `INT_MAX` which is safe, then one extra `x`
in the denominator restores the correct value.

**Iterative variant:** maintain a running
`result` and repeatedly square `x` while
halving `n`, multiplying `result` by `x`
whenever `n` is odd.

```python
result = 1.0
if n < 0:
    x, n = 1 / x, -n
while n:
    if n % 2:
        result *= x
    x *= x
    n //= 2
return result
```

---

## Pattern 4: Cycle Detection via Visited Set

Sequences defined by applying a fixed function
repeatedly either terminate at a fixed point or
cycle. A hash set catches the cycle in O(1)
per step.

### Happy Number
A number is happy if repeatedly replacing it
with the sum of squares of its digits eventually
reaches 1. Otherwise the sequence cycles.

- **File:** `happy-number.py`
- **Technique:** recursion with a visited set.
  Return `True` when `n == 1`; return `False`
  when `n` is seen again.
- **Complexity:** O(log n) per step (digit
  count shrinks), O(log n) unique values before
  cycle or termination.

```python
visited = set()
while n != 1:
    if n in visited:
        return False
    visited.add(n)
    n = sum(int(d) ** 2 for d in str(n))
return True
```

**Floyd's cycle variant:** use slow and fast
pointers instead of a set to achieve O(1) space.
Both advance via the same `digit_square_sum`
function; if they meet and the value is not 1,
it is a cycle.

---

## Pattern 5: Geometry via Frequency Map

Store point frequencies in a hash map. For
geometric queries, enumerate candidate shapes
analytically and look up whether the required
corners exist.

### Detect Squares
Support `add(point)` and `count(query)`.
`count` returns the number of axis-aligned
squares that have `query` as one corner.

- **File:** `detect-squares.py`
- **Key insight:** for an axis-aligned square,
  the diagonal uniquely determines all four
  corners. Given query point `(x1, y1)` and
  a diagonal candidate `(x2, y2)`, the square
  exists iff `|x1-x2| == |y1-y2|` (equal,
  nonzero side length) and both remaining
  corners `(x1, y2)` and `(x2, y1)` are in
  the point map.
- **Count:** multiply the frequencies of all
  three non-query corners (duplicates form
  distinct squares).
- **Complexity:** `add` O(1); `count` O(n)
  where n is the number of distinct points.

```python
for (x2, y2), freq in self.points.items():
    x_dist = abs(x1 - x2)
    y_dist = abs(y1 - y2)
    # Equal nonzero distances = valid diagonal.
    if x_dist == y_dist and x_dist > 0:
        c1 = (x1, y2)
        c2 = (x2, y1)
        if c1 in self.points and c2 in self.points:
            count += (
                freq
                * self.points[c1]
                * self.points[c2]
            )
```

---

## Pattern Recognition Guide

- **Rearrange a matrix without extra space**
  -> Pattern 1: decompose into transpose
  and row-reverse steps (Rotate Image)

- **Visit every cell exactly once in order**
  -> Pattern 1: shrinking-boundary traversal
  (Spiral Matrix)

- **Propagate a flag across rows and columns**
  -> Pattern 1: two-pass collect-then-apply
  (Set Matrix Zeroes)

- **Increment or build a large number by digit**
  -> Pattern 2: right-to-left carry propagation
  (Plus One, Multiply Strings)

- **Raise a number to a large power efficiently**
  -> Pattern 3: halving recurrence O(log n)
  (Pow(x, n))

- **Detect whether a sequence terminates or loops**
  -> Pattern 4: visited set or Floyd's
  two-pointer cycle detection (Happy Number)

- **Count geometric shapes from a point cloud**
  -> Pattern 5: enumerate diagonal candidates,
  look up remaining corners in a freq map
  (Detect Squares)

---

## Complexity Summary

- **Rotate Image:** O(n²) time, O(1) space.
- **Spiral Matrix:** O(m*n) time, O(1) space.
- **Set Matrix Zeroes:** O(m*n) time, O(m+n)
  space; O(1) with first-row/col flag trick.
- **Plus One:** O(n) worst case, O(1) average.
- **Multiply Strings:** O(m+n) time, O(1) space.
- **Pow(x, n):** O(log n) time and stack space.
- **Happy Number:** O(log n) per step, O(log n)
  space; O(1) with Floyd's two-pointer.
- **Detect Squares add:** O(1).
- **Detect Squares count:** O(n) per query.
