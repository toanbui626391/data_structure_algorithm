"""
strategy to solve the problem
    
    problem: find diameter of binary tree
        diameter of binary tree is length of the longest path of the binary tree
        length of path is the number of edge in that path
    why
        using dfs
            we have to know how to compute the deft of a tree
            diameteer of a path through a node equal to sum of the max depth of subtree on the left and on the right
            res = max(res, max(dfs(root.right), dfs(root.left)))

"""

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res

            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right)

            return 1 + max(left, right)

        dfs(root)
        return res