"""
Given an array nums containing n+1 integers in
[1, n], find the one duplicate number. Use O(1)
extra space; do not modify the array.

Example:
  Input:  nums=[1,3,4,2,2]
  Output: 2

Constraints:
  Treat the array as a linked list; use Floyd's cycle detection.
"""


class Solution:
    def findDuplicate(self, nums: "List[int]") -> int:
        slow = 0
        fast = 0
        # Phase 1: find the intersection inside the cycle.
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 2: find the cycle entrance (duplicate value).
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
