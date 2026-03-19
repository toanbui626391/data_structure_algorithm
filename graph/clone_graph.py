"""
Given a reference to a node in a connected undirected
graph, return a deep copy (clone) of the graph.

Example:
  Input:  adjList=[[2,4],[1,3],[2,4],[1,3]]
  Output: deep copy with same adjacency structure

Constraints:
  A hashmap from old nodes to copies avoids reprocessing.
"""


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
