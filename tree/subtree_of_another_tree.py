"""
Problem:
Subtree of Another Tree - Given the roots of two
binary trees `root` and `subRoot`, return True if
there is a subtree of `root` with the same structure
and node values as `subRoot`, and False otherwise.

Examples:
Input:
root    = [3, 4, 5, 1, 2]
subRoot = [4, 1, 2]

Output: True

Input:
root    = [3, 4, 5, 1, 2, null, null, null, null, 0]
subRoot = [4, 1, 2]

Output: False

Constraints:
- The number of nodes in root is in [1, 2000].
- The number of nodes in subRoot is in [1, 1000].
- -10^4 <= root.val, subRoot.val <= 10^4
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Approach: Recursive DFS with a helper.

    At each node in 'root', check if the tree
    rooted there is identical to 'subRoot'.
    If not, recursively check the left and right
    subtrees.

    Two helpers:
    - isSubtree: traverse every node of 'root'.
    - isSameTree: compare two trees node-by-node.
    """

    def isSubtree(
        self,
        root: Optional[TreeNode],
        subRoot: Optional[TreeNode],
    ) -> bool:
        # An empty root cannot contain any subtree.
        if not root:
            return False

        # Check if the tree rooted here matches.
        if self.isSameTree(root, subRoot):
            return True

        # Otherwise, check left and right subtrees.
        left_has_sub = self.isSubtree(
            root.left, subRoot
        )
        right_has_sub = self.isSubtree(
            root.right, subRoot
        )
        return left_has_sub or right_has_sub

    def isSameTree(
        self,
        s: Optional[TreeNode],
        t: Optional[TreeNode],
    ) -> bool:
        # Both None means they match at this node.
        if not s and not t:
            return True

        # One is None and the other is not: mismatch.
        if not s or not t:
            return False

        # Values must match, and both subtrees must too.
        values_match = s.val == t.val
        left_match = self.isSameTree(s.left, t.left)
        right_match = self.isSameTree(s.right, t.right)
        return values_match and left_match and right_match


if __name__ == "__main__":
    sol = Solution()

    # Build root = [3, 4, 5, 1, 2]
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)

    # Build subRoot = [4, 1, 2]
    sub = TreeNode(4)
    sub.left = TreeNode(1)
    sub.right = TreeNode(2)

    result = sol.isSubtree(root, sub)
    print(f"Is subtree: {result}")
    # Expected: True
