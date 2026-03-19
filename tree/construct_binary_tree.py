"""
Given preorder and inorder traversal arrays of a
binary tree, construct and return the binary tree.

Example:
  Input:  preorder=[3,9,20,15,7], inorder=[9,3,15,20,7]
  Output: [3,9,20,null,null,15,7]

Constraints:
  preorder[0] is always the current root; inorder splits
  the left and right subtrees around it.
"""

from typing import List, Optional


class Solution:
    def buildTree(
        self,
        preorder: List[int],
        inorder: List[int],
    ) -> Optional["TreeNode"]:
        # An empty traversal means an empty subtree.
        if not preorder or not inorder:
            return None
        # The first preorder element is the current root.
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        # Slice preorder and inorder for each subtree.
        root.left = self.buildTree(
            preorder[1: mid + 1], inorder[:mid]
        )
        root.right = self.buildTree(
            preorder[mid + 1:], inorder[mid + 1:]
        )
        return root
