"""
strategy to solve the problem
    problem: traverse the binary tre by level order
    why
        use bfs(root) because we want traverse the tree by level
            queue (deque): to keep the nodes to be process
                first in first ourt
"""

from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        q = deque()
        if root:
            q.append(root)

        while q:
            val = [] #hold vals of current level

            for i in range(len(q)): #process nodes at the current level
                node = q.popleft()
                val.append(node.val)
                #collect nodes for the next level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(val)
        return res