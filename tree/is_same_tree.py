"""
Given the roots of two binary trees, check if they
are the same tree (structurally identical with the
same node values).

Example:
  Input:  p=[1,2,3], q=[1,2,3]
  Output: True

Constraints:
  Two null nodes are trivially the same tree.
"""


class Solution:
    def isSameTree(
        self,
        p: "Optional[TreeNode]",
        q: "Optional[TreeNode]",
    ) -> bool:
        # Two null nodes are equal.
        if not p and not q:
            return True
        # Both nodes must exist and hold the same value.
        if p and q and p.val == q.val:
            return (
                self.isSameTree(p.left, q.left)
                and self.isSameTree(p.right, q.right)
            )
        return False
