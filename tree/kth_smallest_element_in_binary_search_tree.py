"""
Given the root of a binary search tree and an
integer k, return the kth smallest value among
all node values.

Example:
  Input:  root=[3,1,4,null,2], k=1
  Output: 1

Constraints:
  In-order traversal of a BST yields values in sorted order.
"""


class Solution:
    def kthSmallest(self, root: "TreeNode", k: int) -> int:
        stack = []
        curr = root

        while stack or curr:
            # Descend to the leftmost unvisited node.
            while curr:
                stack.append(curr)
                curr = curr.left
            # Process the smallest remaining node.
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            # Move to the right subtree.
            curr = curr.right
