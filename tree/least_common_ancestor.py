"""
strategy to solve the problem
    problem: find the lowest common ancestor in binary search tree
        binary search tree: is binary tree which left child < root while right child > root
        binary search tree help search number faster
    why:
        root is common ancestor of p and q if p.val <= root.val <= q.val
        so continue to search if both p and q is the same side of current node 
    variables:
        cur (TreeNode): to move between node from root

"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur