"""
strategy to solve the problem
    problem: given 
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = root.val

        # return max path sum without split
        def dfs(root):
            nonlocal res
            if not root:
                return 0


            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            #why min sum is zero. 
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # compute max path sum WITH split or path sum go through the current node
            res = max(res, root.val + leftMax + rightMax)

            #the value of current node, when it not split
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res