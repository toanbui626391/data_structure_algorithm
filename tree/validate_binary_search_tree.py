"""
strategy to solve the problem
    problem: validate the binary search tree
        binary search tree: is binary tree which left subtree is smaller than root and root is smaller than right subTree
    why:
        using dfs(root, left_limit, right_limit)
        on the left subTree we will know the right limit from root
        on the right subTree we will know the left limmit from root

"""
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def valid(node, left, right):
            #base case, None tree is a valida BTS
            if not node: 
                return True
            #check for a tree is not a valid BST
            if not (node.val < right and node.val > left): #condition to return False
                return False
            # a binary tree is valid BST when it subTre is also valid
            return valid(node.left, left, node.val) and valid(
                node.right, node.val, right
            )

        return valid(root, float("-inf"), float("inf"))