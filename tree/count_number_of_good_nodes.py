"""
In a binary tree, a node is "good" if no node
on the path from root to that node has a greater
value. Return the number of good nodes.

Example:
  Input:  root=[3,1,4,3,null,1,5]
  Output: 4

Constraints:
  DFS carries the running max to evaluate each node.
"""


class Solution:
    def goodNodes(self, root: "TreeNode") -> int:
        def dfs(node, max_val):
            # An empty subtree contributes 0 good nodes.
            if not node:
                return 0

            # A node is good when its value is >= path max.
            count = 1 if node.val >= max_val else 0
            max_val = max(max_val, node.val)
            count += dfs(node.left, max_val)
            count += dfs(node.right, max_val)
            return count

        return dfs(root, root.val)
