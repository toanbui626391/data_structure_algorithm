"""
Given a reference to a node in a connected undirected
graph, return a deep copy (clone) of the graph.

Example:
  Input:  adjList=[[2,4],[1,3],[2,4],[1,3]]
  Output: deep copy with same adjacency structure

Constraints:
  A hashmap from old nodes to copies avoids reprocessing.
"""

from collections import deque


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        # Maps each original node to its copy.
        old_to_new = {}

        def dfs(node):
            # Return existing copy if already cloned.
            if node in old_to_new:
                return old_to_new[node]
            # Create a copy and register it before recursing.
            copy = Node(node.val)
            old_to_new[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy

        return dfs(node) if node else None

    def cloneGraphBFS(self, node: "Node") -> "Node":
        if not node:
            return node

        # Maps each original node to its copy.
        clones = {node: Node(node.val)}
        queue = deque([node])

        while queue:
            curr = queue.popleft()

            for nxt in curr.neighbors:
                if nxt not in clones:
                    clones[nxt] = Node(nxt.val)
                    queue.append(nxt)

                # Link the copies.
                clones[curr].neighbors.append(clones[nxt])

        return clones[node]
