
"""
strategy to solve the problem
    why:
        using slow, fast strategy. both slow and fast start at head.
        if slow == fast then we have cycled linked list
    variables:
        slow, fast (ListNode): to move slow and fast along the linked list
"""
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False