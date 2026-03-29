"""
Given the root of a binary tree, return its
maximum depth (number of nodes along the longest
path from root to a leaf node).

Example:
  Input:  root=[3,9,20,null,null,15,7]
  Output: 3

Constraints:
  Depth = 1 + max(left depth, right depth).
"""

from collections import deque


class Solution:
    def maxDepth(self, root: "TreeNode") -> int:
        # BFS counts levels layer by layer.
        queue = deque()
        level = 0
        if root:
            queue.append(root)

        while queue:
            # Process all nodes at the current level.
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return level

    def maxDepthDFS(self, root: "TreeNode") -> int:
        # Base case: empty node contributes depth 0.
        if not root:
            return 0

        # Recurse on both children.
        left_depth = self.maxDepthDFS(root.left)
        right_depth = self.maxDepthDFS(root.right)

        # This node adds 1 to the deeper subtree's depth.
        return 1 + max(left_depth, right_depth)
