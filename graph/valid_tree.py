"""
strategy to solve the problem
    problem: 
        given a list of edges. check is it a valid tree
    why:
        using union find algorithm to count connected component by build tree
        if connected component is 1 then this is a valid tree with node redundant egdes

"""
class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def __find(self, n: int) -> int: #help function which only use by other function __function_name()
        """
        find root of node. we travese the graph tree and find root if the current node is it's parent
        """
        while n != self.parents.get(n, n):#
            n = self.parents.get(n, n)
        return n

    def __connect(self, n: int, m: int) -> None:
        pn = self.__find(n)
        pm = self.__find(m)
        if pn == pm:
            return
        if self.heights.get(pn, 1) > self.heights.get(pm, 1):
            self.parents[pn] = pm
        else:
            self.parents[pm] = pn
            self.heights[pm] = self.heights.get(pn, 1) + 1
        self.components -= 1

    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # init here as not sure that ctor will be re-invoked in different tests
        self.parents = {} #{node: node's_parent}
        self.heights = {} #{node: size}
        self.components = n #number of component

        for e1, e2 in edges:
            if self.__find(e1) == self.__find(e2):  # 'redundant' edge
                return False
            self.__connect(e1, e2)

        return self.components == 1  # forest contains one tree


