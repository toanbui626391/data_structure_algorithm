"""
Given n nodes and a list of edges, return true if
the edges form a valid tree (connected, no cycles).

Example:
  Input:  n=5, edges=[[0,1],[0,2],[0,3],[1,4]]
  Output: True

Constraints:
  A valid tree has exactly one connected component and no cycles.
"""

from typing import List


class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        # Condition 1: A valid tree must have exactly n - 1 edges.
        if len(edges) != n - 1:
            return False
            
        # Initialize Union-Find structures
        parent = [i for i in range(n)]
        rank = [1] * n
        
        def find(node):
            # Path Compression
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
            
        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)
            
            # Cycle detected
            if root1 == root2:
                return False
                
            # Union by Rank
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1
                
            return True

        # Process all edges
        for u, v in edges:
            if not union(u, v):
                # If union returns False, a cycle was found
                return False
                
        # If n-1 edges are added without cycles, it's guaranteed to be a single component
        return True
