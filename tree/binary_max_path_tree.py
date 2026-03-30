"""
Given the root of a binary tree, return the maximum
path sum. A path is any sequence of nodes where
each pair is connected, and can start/end anywhere.

Example:
  Input:  root=[-10,9,20,null,null,15,7]
  Output: 42

Constraints:
  At each node, the split path = left max + right max + val.
"""


class Solution:
    def maxPathSum(self, root: "TreeNode") -> int:
        result = root.val

        def dfs(root):
            nonlocal result
            if not root:
                return 0

            left_max = dfs(root.left)
            right_max = dfs(root.right)
            # Negative contributions are ignored.
            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            # Update result with path through this node.
            result = max(result, root.val + left_max + right_max)

            # Return the best single-arm extension upward.
            return root.val + max(left_max, right_max)

        dfs(root)
        return result
