#strategy to solve the problem
    #why:
        #using sliding window strategy
            #when right pointer move to the end then lefft.next is the nth node need to remove
    #varialbe
        #dummy (ListNode): to make right - left = n 
        #right, left (ListNode): as pointer 
        #left = dummy.
    #error notes:
        #right = head and left = dummy. we have to make sure left - right = n
        #left have to start from dummy ListNode(0, head) to avoid NonType error because pointer is out of range
        #if you move n time then the distin between start and current position is n - 1.
        #using dummy left, we have make different position is n - 1+ 1 = n
        #this is very helpful to remove nth position from the end
        #we have to grow and return dummy.next or return the head of self grow linked list
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        right = head
        left = dummy
        #move right pointer n time from head
        while n > 0:
            right = right.next
            n -= 1

        #move right pointer to the end
        while right:
            left = left.next
            right = right.next
        #delete
        left.next = left.next.next
        return dummy.next