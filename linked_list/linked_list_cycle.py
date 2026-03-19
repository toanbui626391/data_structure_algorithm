"""
Given the head of a linked list, return true if
the linked list has a cycle in it.

Example:
  Input:  head=[3,2,0,-4] with cycle at pos 1
  Output: True

Constraints:
  Floyd's algorithm detects a cycle in O(n) with O(1) space.
"""


class Solution:
    def hasCycle(
        self, head: "Optional[ListNode]"
    ) -> bool:
        # Slow moves one step; fast moves two steps.
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # If they meet, there is a cycle.
            if slow == fast:
                return True
        return False
