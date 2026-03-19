"""
Design a time-based key-value store. set() stores
(key, value, timestamp). get() returns the value
with the largest timestamp <= the given timestamp.

Example:
  set("foo","bar",1); get("foo",1) -> "bar"
  get("foo",3) -> "bar"

Constraints:
  Timestamps are set in strictly increasing order per key.
"""

from collections import defaultdict


class TimeMap:
    def __init__(self):
        """
        Initialize the data structure.
        """
        # Each key maps to a list of (value, timestamp) pairs.
        self.keeper = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keeper[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        values = self.keeper[key]

        left, right = 0, len(values) - 1

        # Binary search for the largest timestamp <= given.
        while left <= right:
            mid = (left + right) // 2
            if timestamp >= values[mid][1]:
                result = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return result
