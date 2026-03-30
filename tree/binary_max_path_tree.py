"""
Problem:
Binary Tree Maximum Path Sum - Given the root
of a binary tree, return the maximum path sum.

A path is any sequence of nodes where each
adjacent pair is connected. A path can start
and end at any node.

Examples:
Input:
root = [-10, 9, 20, null, null, 15, 7]

Output: 42 (path: 15 -> 20 -> 7)

Constraints:
- The number of nodes is in [1, 3 * 10^4].
- -1000 <= Node.val <= 1000
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Standard DFS updating a class-level variable.
    
    The DFS returns only the max single-arm path
    to extend upward. It updates 'self.max_sum'
    with the max split path extending across the node.
    """

    def __init__(self):
        self.max_sum = float("-inf")

    def maxPathSum(
        self, root: Optional[TreeNode]
    ) -> int:

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            # Recurse into children first.
            left_arm = max(dfs(node.left), 0)
            right_arm = max(dfs(node.right), 0)

            # Update global max with split path.
            split_path = node.val + left_arm + right_arm
            self.max_sum = max(self.max_sum, split_path)

            # Return best single arm extending upward.
            return node.val + max(left_arm, right_arm)

        dfs(root)
        return int(self.max_sum)


if __name__ == "__main__":
    sol = Solution()

    # Build tree: [-10, 9, 20, null, null, 15, 7]
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    result = sol.maxPathSum(root)
    print(f"Max path sum: {result}")
    # Expected: 42 (path: 15 -> 20 -> 7)
