"""
strategy to solve the problem:
    problem: check if two binary tree are same tree.
        two binary tree are structurally identical
        nodes have the same value
    why:
        two None node is the same tree
        two tree is the same if its not None and have the same value else it is not the same

"""
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False