"""
Given the head of a linked list L0->L1->...->Ln,
reorder it to L0->Ln->L1->Ln-1->... in-place.

Example:
  Input:  head=[1,2,3,4]
  Output: [1,4,2,3]

Constraints:
  Find mid, reverse second half, then interleave both halves.
"""


class Solution:
    def reorderList(self, head: "ListNode") -> None:
        # Find the middle using slow/fast pointers.
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half in-place.
        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # Interleave first and reversed second halves.
        first = head
        second = prev
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
