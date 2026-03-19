"""
You are given two non-empty linked lists representing
two non-negative integers stored in reverse order.
Add the two numbers and return the sum as a linked list.

Example:
  Input:  l1=[2,4,3], l2=[5,6,4]
  Output: [7,0,8]  (342 + 465 = 807)

Constraints:
  A carry variable handles the digit overflow each step.
"""


class Solution:
    def addTwoNumbers(
        self,
        l1: "Optional[ListNode]",
        l2: "Optional[ListNode]",
    ) -> "Optional[ListNode]":
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            digit_sum = val1 + val2 + carry
            carry = digit_sum // 10
            curr.next = ListNode(digit_sum % 10)

            # Advance the result pointer and both inputs.
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
