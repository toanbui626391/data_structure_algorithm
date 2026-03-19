"""
Given the head of a singly linked list, reverse
the list and return the reversed list's head.

Example:
  Input:  head=[1,2,3,4,5]
  Output: [5,4,3,2,1]

Constraints:
  Reverse in-place by redirecting each node's next pointer.
"""


class Solution:
    def reverseList(
        self, head: "Optional[ListNode]"
    ) -> "Optional[ListNode]":
        prev = None
        curr = head

        while curr:
            # Save next before overwriting the pointer.
            temp = curr.next
            curr.next = prev
            # Advance both pointers for the next iteration.
            prev = curr
            curr = temp

        return prev
