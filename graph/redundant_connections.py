"""
Given a graph that was a tree with one extra edge
added, find and return that redundant edge.

Example:
  Input:  edges=[[1,2],[1,3],[2,3]]
  Output: [2,3]

Constraints:
  Union-Find detects the first edge that connects two already-joined nodes.
"""

from typing import List


class Solution:
    def findRedundantConnection(
        self, edges: List[List[int]]
    ) -> List[int]:
        # rank tracks tree sizes for union by rank.
        rank = {}
        # parent maps each node to its root representative.
        parent = {}
        for idx in range(1, len(edges) + 1):
            rank[idx] = 1
            parent[idx] = idx

        def find_root(node):
            """
            Return the root of node using path compression.
            """
            p = parent[node]
            while p != parent[p]:
                # Compress path by skipping one level.
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        for first, second in edges:
            root_first = find_root(first)
            root_second = find_root(second)
            # Same root means this edge is redundant.
            if root_first == root_second:
                return [first, second]
            # Union by rank to keep trees shallow.
            if rank[root_first] > rank[root_second]:
                parent[root_second] = root_first
                rank[root_first] += rank[root_second]
            else:
                parent[root_first] = root_second
                rank[root_second] += rank[root_first]
