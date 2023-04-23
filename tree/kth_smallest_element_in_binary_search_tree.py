"""
strategy to solve the problem:
    problem: get kth smallest elements in binary search tree
        binary search tree: binary tree which left subTree is smaller than right subTree
    why:
        using stack and cur node
            stack to keep nodes to be process by order. stack mean first in last out
            cur to move to node in binary tree
        using dfs but priority left move
    opertions:
        traverse along the left subTre
        when to pop and process node
        when to consider right subTree of the current processing node

"""

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        curr = root

        while stack or curr: #cur condition for mostly start
            while curr:
                stack.append(curr)
                curr = curr.left
            #process node when traversal all depth
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            #move right
            curr = curr.right