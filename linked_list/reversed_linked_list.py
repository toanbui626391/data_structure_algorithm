#strategy to solve the problem
    #why:
        #for each node we just need to change direction of linked list
        #for each iteration we need prev, curr and temp node to do it
        #start with prev, curr = None, head. iterate through linked list and change direction of current node
    #variables:
        #prev, curr, temp (ListNode)
    #error notes:
        #curr = temp. because curr.next have been change before

#############################reference solution
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            #change direction
            temp = curr.next
            curr.next = prev
            #update for next iteration
            prev = curr
            curr = temp

        return prev
