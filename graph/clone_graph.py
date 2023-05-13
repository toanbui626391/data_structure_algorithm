"""
strategy to solve the problem
    problem: 
        make a clone of a graph
        Node(val, neighbors)
    why:
        using newToOld hashMap to keep track of new and it copy
        make a copy if have not do it yet. connect copy with its neighbor
        remember to check the edge case when input node is None
        dfs(node):
            give copy node if input node exist in the map
            normal case. make copy node and add to the map. build neighbors for for copy node
"""
class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        #clone graph from starting node
        oldToNew = {} #maping between node and copied node

        def dfs(node):
            #base case, get the new node from oldToNew
            if node in oldToNew:
                return oldToNew[node]
            #make a copy and add to newToNew hashMap
            copy = Node(node.val)
            oldToNew[node] = copy #for dict, key can be a instance of object
            #get neighbor node from original node, and add copy neighbors of the copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        #check a valid node before run dfs
        return dfs(node) if node else None
