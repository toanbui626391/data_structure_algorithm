"""
Given the root of a binary tree, invert the tree
and return its root.

Example:
  Input:  root=[4,2,7,1,3,6,9]
  Output: [4,7,2,9,6,3,1]

Constraints:
  Swap left and right children at every node recursively.
"""


class Solution:
    def invertTree(
        self, root: "Optional[TreeNode]"
    ) -> "Optional[TreeNode]":
        # An empty subtree is already inverted.
        if not root:
            return None
        # Swap left and right children at this node.
        root.left, root.right = root.right, root.left
        # Recurse into both subtrees.
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
