"""
Given a linked list, reverse the nodes in groups
of k at a time and return the modified list.

Example:
  Input:  head=[1,2,3,4,5], k=2
  Output: [2,1,4,3,5]

Constraints:
  A dummy head and group pointers manage reversal boundaries.
"""


class Solution:
    def reverseKGroup(
        self,
        head: "Optional[ListNode]",
        k: int,
    ) -> "Optional[ListNode]":
        dummy = ListNode(0, head)
        prev_group = dummy
        while True:
            kth = self.get_kth_node(prev_group, k)
            if not kth:
                break
            next_group = kth.next

            # Reverse the current group of k nodes.
            prev = kth.next
            curr = prev_group.next
            while curr != next_group:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Reconnect the reversed group to the rest.
            tmp = prev_group.next
            prev_group.next = kth
            prev_group = tmp

        return dummy.next

    def get_kth_node(self, curr, k):
        # Walk k steps from curr; return None if list is short.
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
