"""
Construct a deep copy of a linked list where each
node has a val, next pointer, and random pointer.

Example:
  Input:  head=[[7,null],[13,0],[11,4],[10,2],[1,0]]
  Output: deep copy of the list

Constraints:
  Two passes: create all copies, then wire next and random.
"""


class Solution:
    def copyRandomList(self, head: "Node") -> "Node":
        # Start with {None: None} to handle tail's next/random.
        old_to_copy = {None: None}

        curr = head
        while curr:
            old_to_copy[curr] = Node(curr.val)
            curr = curr.next

        # Assign next and random using the mapping.
        curr = head
        while curr:
            copy = old_to_copy[curr]
            copy.next = old_to_copy[curr.next]
            copy.random = old_to_copy[curr.random]
            curr = curr.next

        return old_to_copy[head]
