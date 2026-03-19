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
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def __find(self, node: int) -> int:
        """
        Find root by following parent links until self-loop.
        """
        while node != self.parents.get(node, node):
            node = self.parents.get(node, node)
        return node

    def __connect(self, node_n: int, node_m: int) -> None:
        root_n = self.__find(node_n)
        root_m = self.__find(node_m)
        if root_n == root_m:
            return
        # Union by height to keep trees shallow.
        if self.heights.get(root_n, 1) > self.heights.get(root_m, 1):
            self.parents[root_n] = root_m
        else:
            self.parents[root_m] = root_n
            self.heights[root_m] = (
                self.heights.get(root_n, 1) + 1
            )
        self.components -= 1

    def valid_tree(
        self, n: int, edges: List[List[int]]
    ) -> bool:
        self.parents = {}
        self.heights = {}
        self.components = n

        for first, second in edges:
            # A redundant edge creates a cycle; not a valid tree.
            if self.__find(first) == self.__find(second):
                return False
            self.__connect(first, second)

        # A valid tree has exactly one connected component.
        return self.components == 1
