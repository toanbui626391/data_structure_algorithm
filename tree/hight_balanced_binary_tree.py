"""
strategy to solve the problem
    problem: check binary tree is hight-balanced
        hight-balanced tree is a tree which the depth different between subtree is smaller or equal to 1
    why:
        using [boolean, height]
            boolean: check the current node balanced or not
            height: height of the current node which help to check for paraent node balance status
        use dfs func because the main function return only boolean
        a None node is a height-balanced

"""
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]
            left = dfs(root.left)
            right = dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]