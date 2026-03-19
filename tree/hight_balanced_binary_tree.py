"""
Given a binary tree, determine if it is
height-balanced (depth difference between left and
right subtrees of every node is at most 1).

Example:
  Input:  root=[3,9,20,null,null,15,7]
  Output: True

Constraints:
  DFS returns both balance status and height together.
"""


class Solution:
    def isBalanced(
        self, root: "Optional[TreeNode]"
    ) -> bool:
        def dfs(root):
            # A null node is balanced with height 0.
            if not root:
                return [True, 0]
            left = dfs(root.left)
            right = dfs(root.right)
            # Balanced only if both subtrees are balanced
            # and their heights differ by at most 1.
            balanced = (
                left[0]
                and right[0]
                and abs(left[1] - right[1]) <= 1
            )
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]
