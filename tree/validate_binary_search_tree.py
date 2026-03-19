"""
Given the root of a binary tree, determine if it
is a valid binary search tree.
Left subtree nodes must be less than root; right
subtree nodes must be greater than root.

Example:
  Input:  root=[2,1,3]
  Output: True

Constraints:
  Each node must fall within an inherited valid range.
"""


class Solution:
    def isValidBST(self, root: "TreeNode") -> bool:
        def valid(node, left_limit, right_limit):
            # An empty node is always a valid BST.
            if not node:
                return True
            # Reject if node's value is out of valid range.
            if not (
                node.val < right_limit
                and node.val > left_limit
            ):
                return False
            # Propagate tighter bounds into each subtree.
            return valid(
                node.left, left_limit, node.val
            ) and valid(node.right, node.val, right_limit)

        return valid(root, float("-inf"), float("inf"))
