"""
strategy to solve the problem:
    #why:
        #1. we need to know how to reverse a linked list
        #we customize 1 to do it iteration for all group in linked list
        #we have to keep track prev_group and nex_group. pre_group is noe which is previous of the current group. next_group is the next node of the current group
        #we also need helper function to find the next node of the current group
        #we also need a dummy node. start dummy node which linked to head.
    #variable
        #dummy (ListNode): which linked to head
        prev_group, kth, next_group (ListNode): to keep track of previous node of group. the kth node of group and the next node of the current group  
    #error notes:
        #start dummy node which is linked to head
        #condition to break loop. while not kth
        #remember to update prev_group.next and prev_group
        #when do reverse, prev = next_group
"""

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev_group = dummy
        while True:
            kth = self.get_kth_node(prev_group, k)
            if not kth:
                break
            next_group = kth.next

            #reverse linked list
            prev, curr = kth.next, prev_group.next
            while curr != next_group:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            #update prev_group for next iteration
            tmp = prev_group.next
            prev_group.next = kth
            prev_group = tmp

        return dummy.next
            

    def get_kth_node(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr