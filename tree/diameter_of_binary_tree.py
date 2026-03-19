"""
Given the root of a binary tree, return the length
of the diameter (the longest path between any two
nodes, measured in number of edges).

Example:
  Input:  root=[1,2,3,4,5]
  Output: 3

Constraints:
  Diameter through a node = left depth + right depth.
"""


class Solution:
    def diameterOfBinaryTree(
        self, root: "Optional[TreeNode]"
    ) -> int:
        result = 0

        def dfs(root):
            nonlocal result
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            # Path through this node spans both subtrees.
            result = max(result, left + right)
            return 1 + max(left, right)

        dfs(root)
        return result
