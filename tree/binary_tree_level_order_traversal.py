"""
Given the root of a binary tree, return the level
order traversal of its nodes' values as a list of
lists, one list per level.

Example:
  Input:  root=[3,9,20,null,null,15,7]
  Output: [[3],[9,20],[15,7]]

Constraints:
  BFS with a deque visits nodes exactly one level at a time.
"""

from collections import deque
from typing import List


class Solution:
    def levelOrder(
        self, root: "TreeNode"
    ) -> List[List[int]]:
        result = []
        queue = deque()
        if root:
            queue.append(root)

        while queue:
            # Collect all values for the current level.
            level_values = []

            for i in range(len(queue)):
                node = queue.popleft()
                level_values.append(node.val)
                # Enqueue children for the next level.
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_values)
        return result
