"""
strategy to solve the problem
    problem: 
        given a graph with n node and n edge. find edge which make this graph to tree (no cycle)
        because we hav n nodes and n edges. we guarantee have one redundant egdes to make graph back to tree (no cycle)
    why:
        using union find algorithm to find number of component in graph

"""
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        rank = {} 
        parent = {} #{node: root_node}
        #init value for rank and parent
        components = len(edges)
        # init rank and parent map
        for i in range(1, len(edges)+1):
            rank[i] = 1
            parent[i] = i
        def find_root(n):
            """
            given node n find 
            """
            p = parent[n]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        #union
        for i,j in edges:
            pi, pj = find_root(i), find_root(j)
            if pi == pj:
                return [i, j]
            if rank[pi] > rank[pj]:
                parent[pj] = pi
                rank[pi] += rank[pj]
            else:
                parent[pi] = pj
                rank[pj] += rank[pi]
            components -= 1
