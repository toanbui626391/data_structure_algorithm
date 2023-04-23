"""

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def serialize(self, root):
        """
        usind dfs(root) traverl depth first search for each node and collect value str(node.val)
        base case collect string N for None
        """
        def dfs(root):
            #base case
            if not root:
                res.append("N")
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        res = []
        dfs(root)
        return ",".join(res)

        
    def deserialize(self, data):
        """
        using dfs() but for each node we popleft() of data (global variable) so right is build correct after left
        """

        def dfs():
            val = data.pop(0)
            #base case
            if val == "N":
                return None
            #build tree with depth first search. left then right
            root = TreeNode(val)
            root.left = dfs()
            root.right = dfs()
            return root
        data = data.split(",")
        return dfs()
