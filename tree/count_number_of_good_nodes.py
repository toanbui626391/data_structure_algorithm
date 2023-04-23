"""
strategy to solve the problem 
    problem: count number of good nodes
        a good nodes is a node which nother nodes larger than it in the path from root to it's selft
    why:
        using dfs(root, maxVal)
            root is the current node
            maxVal to keep the current maxVal of path from root
            res (int) or count to keep track of the current count
        the number of good nodes equal: current node status (1 or 0) + number of good nodes in left subTree + right subTree
"""
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxVal):
            if not node: #the base case
                return 0

            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res

        return dfs(root, root.val)