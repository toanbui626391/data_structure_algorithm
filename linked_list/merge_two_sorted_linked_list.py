#strategy to solve the problem:

    #why:
        #because each linked list is sorted, we can grow a sorted linked list by compare each element in the two linked list to decide which element is on the growing linked list
        #by default sorted is increasing value    
#variables:
        #dummy (ListNode): dummy starting node
        #tail (ListNode): current node to grow for each iteration

#############################################reference solution
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                #grow new node and update for next iteration
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            #prepare for next iteration    
            tail = tail.next

        #handle remaining linked list
        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next