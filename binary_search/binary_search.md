# Binary Search Algorithm

## What Is It?

Binary Search is an efficient algorithm for
finding an item from a sorted list of items.
Instead of checking elements one by one from
the beginning (O(N) time), it repeatedly
divides the search interval in half.

---

## Core Idea

The core idea is **Search Space Reduction**.
Because the data is sorted (or follows a strict
monotonic condition), checking the middle
element allows us to instantly eliminate half
of the remaining possibilities.

If the target value is less than the middle
element, we narrow the interval to the lower
half. Otherwise, we narrow it to the upper
half. This logarithmic halving results in an
ultra-fast O(log N) runtime.

---

## General Implementation (Python)

A standard binary search loops while the
`left` pointer is less than or equal to the
`right` pointer.

```python
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        # Using (right - left) // 2 prevents
        # integer overflow in languages like
        # Java/C++, though typical (l+r)//2
        # is fine in standard Python.
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid  # Target found
            
        elif arr[mid] < target:
            # Target is in the right half
            left = mid + 1
            
        else:
            # Target is in the left half
            right = mid - 1

    return -1  # Target not found
```

---

## Suitable Problem Types

Binary search goes far beyond simply finding a
number in an array. It is used whenever there
is a **monotonic property** (a clear threshold
where conditions switch from False to True).

### 1. Finding Exact Matches
- **Standard Search:** Finding a target number
  in a sorted array.
- **Search in 2D Matrix:** Treating a sorted
  2D grid like a flattened 1D array.

### 2. Finding Boundaries
- **First Bad Version:** Finding the exact
  commit where a software build broke.
- **Find First and Last Position:** Finding
  the start and end indices of a duplicate
  number in a sorted array `[...3,3,3...]`.

### 3. Binary Search on Answer
- **Koko Eating Bananas:** Finding the minimum
  eating speed `k`. We binary search the space
  of possible speeds `[1 ... max(piles)]`. If
  speed `X` works, any speed `> X` also works.
- **Split Array Largest Sum:** Minimizing the
  maximum sum among subarrays by "guessing" an
  answer and checking if it's statistically
  valid.

### 4. Search in Rotated Arrays
- **Find Minimum in Rotated Sorted Array:**
  Comparing `mid` with the `right` edge to
  determine which half contains the pivot
  point where the array was disconnected.

---

## Complexity

- **Time:** O(log N). The search space is
  cut in half during every single iteration.
  Searching 1 billion items takes ~30 steps.
- **Space:** O(1) for the iterative approach.
  Requires O(log N) if implemented recursively
  due to the internal call stack.
