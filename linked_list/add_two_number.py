"""
strategy to solve the problem
    why:
        grow new linked list by loop through each list
        using divide operation: /, //, %
    #variables:
        dummy, curr (ListNode): to start and grow new linked list
        carry (int): to calculate sum of next interation
    #error note
        #check for case where l1 and l2 must not None
        #condition to break loop
            while l1 or l2 or carry
"""
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            val = val1+val2 + carry
            carry = val // 10
            curr.next = ListNode(val%10)

            #update
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next