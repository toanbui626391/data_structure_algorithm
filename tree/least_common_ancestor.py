"""
Given a BST and two nodes p and q, find their
lowest common ancestor (the deepest node that is
an ancestor of both p and q).

Example:
  Input:  root=[6,2,8,0,4,7,9], p=2, q=8
  Output: 6

Constraints:
  BST ordering lets us decide which side to descend.
"""


class Solution:
    def lowestCommonAncestor(
        self,
        root: "TreeNode",
        p: "TreeNode",
        q: "TreeNode",
    ) -> "TreeNode":
        curr = root

        while curr:
            # Both nodes are in the right subtree.
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # Both nodes are in the left subtree.
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            # Nodes split across curr; curr is the LCA.
            else:
                return curr
