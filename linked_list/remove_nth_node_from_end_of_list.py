"""
Given the head of a linked list, remove the nth
node from the end and return the head.

Example:
  Input:  head=[1,2,3,4,5], n=2
  Output: [1,2,3,5]

Constraints:
  A dummy head plus two pointers n apart makes removal clean.
"""


class Solution:
    def removeNthFromEnd(
        self,
        head: "Optional[ListNode]",
        n: int,
    ) -> "Optional[ListNode]":
        dummy = ListNode(0, head)
        right = head
        left = dummy

        # Advance right n steps ahead of left.
        while n > 0:
            right = right.next
            n -= 1

        # Move both until right reaches the end.
        while right:
            left = left.next
            right = right.next

        # left.next is now the node to remove.
        left.next = left.next.next
        return dummy.next
