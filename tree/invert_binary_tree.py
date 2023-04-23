"""
strategy to solve the problem:
    problem: invert binary three. 
        binary three (val, left, right)
    why using dfs:
        we can do recursive and invert three (convert left to right and right to left)

"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #base case, when to stop
        if not root:
            return None
        #invert tree at one node
        root.left, root.right = root.right, root.left
        #recursively with next left and right node
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root #return root after all recursively invert subtree