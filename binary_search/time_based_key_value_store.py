"""
Problem: Time Based Key-Value Store

Design a time-based key-value store. set() stores
(key, value, timestamp). get() returns the value
with the largest timestamp <= the given timestamp.

Example:
  set("foo","bar",1); get("foo",1) -> "bar"
  get("foo",3) -> "bar"

Approach: Hash Map + Binary Search
  - Map each key to a list of (timestamp, value).
  - Because timestamps are strictly increasing,
    the list is naturally sorted.
  - Binary search the list to find the largest
    timestamp <= the target timestamp.
"""

from collections import defaultdict


class TimeMap:
    def __init__(self):
        # Maps key -> list of (timestamp, value)
        self.store = defaultdict(list)

    def set(
        self, key: str, value: str, timestamp: int
    ) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])

        left = 0
        right = len(values) - 1

        while left <= right:
            mid = left + (right - left) // 2
            
            # If mid timestamp is <= target, it's valid
            if values[mid][0] <= timestamp:
                res = values[mid][1]
                # Try to find a closer (larger) one
                left = mid + 1
            else:
                # Mid timestamp is too large
                right = mid - 1
                
        return res
