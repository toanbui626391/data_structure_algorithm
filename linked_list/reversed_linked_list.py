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
"""
linked list:
    singly linked list: 
        a list with multiple node each node linked together with pointer (node.next)
        node (val, next)
        can only move in one direction
    doubly linked list
        like singly linked list with node (val, prev, next) therefore, we can move backford or forward

reverse a linked list:
    #we just need to change curr.next to prev node. but we need a temp variable to do it
    #change direction of current node
    temp = curr.next
    cur.next = prev
    #prepare for next iteration
    prev = curr
    curr = temp
"""
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
