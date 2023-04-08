"""
strategy to solve the problem
    problem: find the max depth of the binary tree
        depth of a binary is the number of node along side the longest path from root to leave node
    why:
        when count from leaf to root node the def of current root equal to, 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        using dfs iteratively
"""

# RECURSIVE DFS
    #go to each node plus 1 for depth
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
###################################################################
"""
strategy to solve max depth of binary search tree

breadth first search:
    queue (deque): to keep track of nodes to be process in order
    in breadth first search we use first in and first out
    while queue:
        for i in range(len(queue)): #to process node in the current level
            node = queue.popleft() 
            #collect nodes from the next level
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        level += 1 #update current level
    
    variables:
        queue (deque)
        level (int)

"""
from collections import deque
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        queue = deque()
        level = 0
        #avoid root is None
        if root:
            queue.append(root)

        while queue:
            for i in range(len(queue)): #get all nodes of the current level
                node = queue.popleft()
                #collect all nodes of next level
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            level += 1 #update current level
        return level
    

"""
solve the max depth of binary tree with iterative depth first search
    why:
        using iterative depth first search.
            stack (node, length)
"""
class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        
        stack = [[root, 1]]
        res = 0

        while stack: #stack will help us which nodes to be process
            node, depth = stack.pop() #first in and first out
            if node:
                stack.append([node.right, depth+1])
                stack.append([node.left, depth+1])
                res = max(res, depth)
        return res
