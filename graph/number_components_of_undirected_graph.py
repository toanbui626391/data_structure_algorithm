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


def countComponents(n: int, edges: list[list[int]]) -> int:
    parent = [i for i in range(n)]
    rank = [1] * n
    
    # We start with n disconnected components
    components = n
    
    def find(node):
        if parent[node] != node:
            # Path compression
            parent[node] = find(parent[node])
        return parent[node]
        
    def union(n1, n2):
        p1, p2 = find(n1), find(n2)
        
        # If they already share the same root, we didn't connect anything new
        if p1 == p2:
            return 0
            
        # Union by rank
        if rank[p2] > rank[p1]:
            parent[p1] = p2
        elif rank[p1] > rank[p2]:
            parent[p2] = p1
        else:
            parent[p1] = p2
            rank[p2] += 1
            
        # We successfully merged two components
        return 1

    # Process each edge
    for n1, n2 in edges:
        # Subtract 1 from components if a merge happened
        components -= union(n1, n2)
        
    return components