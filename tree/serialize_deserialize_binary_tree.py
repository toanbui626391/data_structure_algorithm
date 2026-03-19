"""
Design an algorithm to serialize and deserialize a
binary tree. The codec must encode to a string and
decode back to the original tree structure.

Example:
  serialize([1,2,3,null,null,4,5]) -> "1,2,N,N,3,4,N,N,5,N,N"
  deserialize("1,2,N,N,3,4,N,N,5,N,N") -> [1,2,3,null,null,4,5]

Constraints:
  DFS pre-order lets serialize and deserialize agree on order.
"""


class Codec:
    def serialize(self, root):
        """
        DFS pre-order: record each value or "N" for null.
        """
        def dfs(root):
            # Represent null nodes with "N".
            if not root:
                collected.append("N")
                return
            collected.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        collected = []
        dfs(root)
        return ",".join(collected)

    def deserialize(self, data):
        """
        Consume tokens left to right; reconstruct left before right.
        """
        def dfs():
            val = tokens.pop(0)
            if val == "N":
                return None
            root = TreeNode(val)
            root.left = dfs()
            root.right = dfs()
            return root

        tokens = data.split(",")
        return dfs()
