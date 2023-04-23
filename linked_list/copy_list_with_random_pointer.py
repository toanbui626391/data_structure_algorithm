"""
strategy to solve the problem
    why:
        using two loop strategy
        first loop to map new node with old node
        second loop to assign value to new code attribute (next, random)

    variable: 
        old_to_copy (dict): to mapping between old and copy node
    error note:
        #start with old_to_copy = {None:None} in case we get tail of linked list
"""
class Solution:
    def copyRandomList(self, head: "Node") -> "Node":
        old_to_copy = {None: None}

        curr = head
        while curr:
            old_to_copy[curr] = Node(curr.val)
            curr = curr.next

        #assign value to attribute next and random of copy node
        curr = head
        while curr:
            copy = old_to_copy[curr]
            copy.next = old_to_copy[curr.next]
            copy.random = old_to_copy[curr.random]
            curr = curr.next

        return old_to_copy[head]