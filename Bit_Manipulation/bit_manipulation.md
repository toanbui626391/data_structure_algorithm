# Bit Manipulation

Bit manipulation operates directly on the binary
representation of integers. It is faster than
arithmetic, avoids extra memory, and reveals
elegant solutions to problems that look complex
at first glance.

---

## Binary Representation

Every integer is stored as a sequence of bits.
Bit positions are numbered from 0 (least
significant) on the right.

```
decimal  13  =  binary  0...01101
                bit pos: ...3 2 1 0
```

Python integers have arbitrary precision, but
most LeetCode bit problems assume 32-bit signed
or unsigned integers.

---

## Core Operators

### AND  `a & b`
Output bit is 1 only when both input bits are 1.

```
  1010          Use to: isolate a bit, test a bit,
& 1100            clear bits (mask off upper bits)
------
  1000
```

### OR  `a | b`
Output bit is 1 when at least one input is 1.

```
  1010          Use to: set a specific bit,
| 0110            merge two bit patterns
------
  1110
```

### XOR  `a ^ b`
Output bit is 1 when exactly one input is 1.

```
  1010          Use to: toggle a bit, cancel
^ 0110            duplicates, find differences
------
  1100
```

### NOT  `~a`
Flips every bit. In Python `~a == -(a+1)` due
to two's complement with arbitrary precision.

### Left Shift  `a << k`
Moves all bits k positions to the left,
filling right with zeros. Equivalent to
multiplying by `2^k`.

```
0001 << 3  =  1000   (1 * 8 = 8)
```

### Right Shift  `a >> k`
Moves all bits k positions to the right,
discarding the lowest k bits. Equivalent to
floor division by `2^k`.

```
1100 >> 2  =  0011   (12 // 4 = 3)
```

---

## Essential XOR Properties

XOR is the most-used operator in bit problems.
Its key properties are:

- `x ^ x = 0`  — a value XOR itself is zero.
- `x ^ 0 = x`  — XOR with zero is identity.
- Commutative: `a ^ b = b ^ a`
- Associative: `(a^b)^c = a^(b^c)`

**Consequence:** XOR-ing a set of values where
every element appears an even number of times
produces 0. Any element appearing an odd number
of times survives.

---

## Common Bit Tricks

### Read the lowest bit
```python
lowest_bit = n & 1   # 1 if odd, 0 if even
```

### Clear the lowest set bit
```python
n = n & (n - 1)
# n-1 flips the lowest set bit and all below it.
# AND with n clears only that bit.
```

This is the fastest way to count set bits
(Brian Kernighan's algorithm): repeat until n=0,
counting iterations.

### Check if n is a power of two
```python
is_power_of_two = n > 0 and (n & (n - 1)) == 0
# A power of two has exactly one set bit.
# n-1 has all lower bits set; AND produces 0.
```

### Isolate bit at position k
```python
bit_k = (n >> k) & 1
```

### Set bit at position k
```python
n = n | (1 << k)
```

### Clear bit at position k
```python
n = n & ~(1 << k)
```

### Toggle bit at position k
```python
n = n ^ (1 << k)
```

### Build a 32-bit mask
```python
mask = (1 << 32) - 1   # 0xFFFFFFFF
# AND with mask keeps only the lowest 32 bits.
```

---

## Pattern 1: XOR to Cancel Duplicates

XOR every element together. Pairs cancel to 0;
the unpaired element survives as the result.
Works because XOR is commutative and associative.

### Single Number
Find the one element that does not appear twice.

- **File:** `single-number.py`
- **Technique:** XOR all elements.
- **Complexity:** O(n) time, O(1) space.

```python
result = 0
for num in nums:
    result ^= num
return result
```

**Trace for `[4, 1, 2, 1, 2]`:**
```
0 ^ 4 = 4
4 ^ 1 = 5
5 ^ 2 = 7
7 ^ 1 = 6   (1 ^ 1 = 0, cancels)
6 ^ 2 = 4   (2 ^ 2 = 0, cancels)
result = 4
```

### Missing Number
Given `nums` containing `n` distinct values
from `[0, n]`, find the missing one.

- **File:** `missing-number.py`
- **Technique:** XOR all indices `1..n` with all
  values. Present values cancel with their index;
  the missing index has no partner.
- **Complexity:** O(n) time, O(1) space.

```python
result = 0
for i in range(1, len(nums) + 1):
    result ^= i
for num in nums:
    result ^= num
return result
```

**Why it works:** every number `1..n` appears
once as an index and once as a value — except the
missing number which appears only as an index.
That index survives after all XORs.

---

## Pattern 2: Bit Counting

Count or accumulate the number of set bits (1s)
in an integer. Two approaches: shift-and-AND for
a single number, or DP reuse across a range.

### Number of 1-Bits (Hamming Weight)
Return the number of set bits in a 32-bit integer.

- **File:** `number-of-1-bits.py`
- **Technique:** repeatedly test the lowest bit
  with `n & 1`, then right-shift to advance.
- **Complexity:** O(32) = O(1).

```python
count = 0
while n != 0:
    count += n & 1
    n >>= 1
return count
```

**Alternative — Brian Kernighan's trick:**
`n & (n-1)` clears the lowest set bit in one
step. Loop until `n == 0`, counting iterations.

```python
count = 0
while n:
    n &= n - 1   # clear lowest set bit
    count += 1
return count
```

This is faster when set bits are sparse because
it skips over zero-bit stretches entirely.

### Counting Bits
Return an array where `result[i]` is the number
of set bits in `i`, for all `i` in `[0, n]`.

- **File:** `counting-bits.py`
- **Technique:** DP reuse.
  `i >> 1` is `i // 2`; its bit count is already
  stored. Add the lowest bit of `i` to get
  `result[i]`.
- **Complexity:** O(n) time, O(n) space.

```python
result = [0] * (n + 1)
for i in range(1, n + 1):
    result[i] = result[i >> 1] + (i & 1)
return result
```

**Why the recurrence works:**
Shifting `i` right by 1 drops the lowest bit.
The count for `i >> 1` is already computed.
Adding back `i & 1` (the dropped bit) gives the
count for `i` in O(1) per element.

---

## Pattern 3: Bit Construction

Build an output integer bit by bit. Typically:
read one bit from the source, place it in the
target, then advance both with shifts.

### Reverse Bits
Reverse the 32 bits of an unsigned integer.

- **File:** `reverse-bits.py`
- **Technique:** for each of 32 iterations,
  left-shift result to make room, OR in the
  lowest bit of `n`, then right-shift `n`.
- **Complexity:** O(32) = O(1).

```python
result = 0
for i in range(32):
    result = (result << 1) | (n & 1)
    n >>= 1
return result
```

**Step trace for `n = 0b1011` (4-bit example):**
```
i=0: result=0b0001, n=0b0101
i=1: result=0b0010, n=0b0010
i=2: result=0b0101, n=0b0001
i=3: result=0b1101, n=0b0000
```

### Reverse Integer
Reverse the decimal digits of a 32-bit signed
integer; return 0 on overflow.

- **File:** `reverse-integer.py`
- **Technique:** uses `1 << 31` to compute the
  32-bit max boundary without hardcoding 2147483648.
- **Complexity:** O(log x) digits.

```python
int_max  = 1 << 31          # 2^31
max_head = int_max // 10    # safe leading value
max_tail = int_max % 10     # safe final digit

while x > 0:
    remainder = x % 10
    if result > max_head or (
        result == max_head
        and remainder >= max_tail
    ):
        return 0
    result = result * 10 + remainder
    x //= 10
```

**Bit usage here:** `1 << 31` computes the
overflow boundary cheaply without a magic number.

---

## Pattern 4: Bitwise Arithmetic

Replace arithmetic operators with bit operations.
XOR gives addition without carry; AND shifted
left gives the carry itself. Repeat until the
carry is zero.

### Sum of Two Integers
Add `a` and `b` without using `+` or `-`.

- **File:** `sum-of-two-integers.py`
- **Technique:** full-adder loop.
  - `a ^ b` — sum of bits, ignoring carry.
  - `(a & b) << 1` — carry bits shifted up.
  - Repeat until carry (`b`) reaches zero.
  - Mask to 32 bits to prevent Python from
    growing integers beyond 32 bits.
- **Complexity:** O(32) = O(1).

```python
mask = (1 << 32) - 1
while b & mask:
    a, b = a ^ b, (a & b) << 1
return a & mask if b != 0 else a
```

**Single-bit trace for `1 + 3`:**
```
a=01, b=11
sum=10 (XOR), carry=10 (AND<<1)

a=10, b=10
sum=00 (XOR), carry=100 (AND<<1)

a=00, b=100
sum=100 (XOR), carry=000

result = 4
```

---

## Pattern Recognition Guide

- **Find unpaired / missing element in O(1) space**
  -> Pattern 1: XOR all values (or XOR
  values with indices)

- **Count set bits in one integer**
  -> Pattern 2: shift-and-AND loop, or
  Brian Kernighan (`n & n-1`)

- **Count set bits across a range `[0, n]`**
  -> Pattern 2: DP with `result[i>>1] + (i&1)`

- **Rearrange or reverse the bits of an integer**
  -> Pattern 3: shift-and-OR construction loop

- **Add integers without arithmetic operators**
  -> Pattern 4: XOR sum + AND-shift carry loop

---

## Complexity Summary

All bit manipulation problems in this directory
run in O(n) or O(1) time because integer width
is bounded (32 bits). Space is always O(1) except
Counting Bits which needs O(n) for the output
array.

- **Single Number:** O(n) time, O(1) space.
- **Missing Number:** O(n) time, O(1) space.
- **Number of 1-Bits:** O(1) time, O(1) space.
- **Counting Bits:** O(n) time, O(n) space.
- **Reverse Bits:** O(1) time, O(1) space.
- **Reverse Integer:** O(log x) time, O(1) space.
- **Sum of Two Integers:** O(1) time, O(1) space.
