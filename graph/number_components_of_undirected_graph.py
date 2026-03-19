"""
Given n nodes and a list of edges forming an
undirected graph, return the number of connected
components.

Example:
  Input:  n=5, edges=[[0,1],[1,2],[3,4]]
  Output: 2

Constraints:
  Union-Find groups nodes by their root, counting distinct roots.
"""

from typing import List


class UnionFind:
    def __init__(self):
        # Maps node to its parent; default is itself.
        self.parent_map = {}

    def findParent(self, node):
        parent = self.parent_map.get(node, node)
        if node != parent:
            # Path compression for efficiency.
            parent = self.parent_map[node] = self.findParent(parent)
        return parent

    def union(self, node_x, node_y):
        self.parent_map[self.findParent(node_x)] = (
            self.findParent(node_y)
        )


class Solution:
    def countComponents(
        self, n: int, edges: List[List[int]]
    ) -> int:
        dsu = UnionFind()
        for first, second in edges:
            dsu.union(first, second)
        return len(
            set(dsu.findParent(node) for node in range(n))
        )
