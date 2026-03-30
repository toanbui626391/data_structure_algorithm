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


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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
        # Reconstruct by popping left-to-right.
        return dfs()


from collections import deque


class CodecBFS:
    """
    Breadth-First Search (Level-Order) Approach.
    
    Uses a queue to process nodes layer by layer.
    """

    def serialize(self, root: "TreeNode") -> str:
        if not root:
            return ""

        collected = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node:
                collected.append(str(node.val))
                # Append children even if None.
                queue.append(node.left)
                queue.append(node.right)
            else:
                collected.append("N")

        return ",".join(collected)

    def deserialize(self, data: str) -> "TreeNode":
        if not data:
            return None

        tokens = data.split(",")
        root = TreeNode(int(tokens[0]))
        queue = deque([root])
        
        # Start looking at children from index 1.
        index = 1
        
        while queue:
            node = queue.popleft()

            # Process left child.
            if tokens[index] != "N":
                node.left = TreeNode(int(tokens[index]))
                queue.append(node.left)
            index += 1

            # Process right child.
            if tokens[index] != "N":
                node.right = TreeNode(int(tokens[index]))
                queue.append(node.right)
            index += 1

        return root


if __name__ == "__main__":
    # Test BFS Implementation
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    codec = CodecBFS()
    serialized = codec.serialize(root)
    print(f"BFS Serialized: {serialized}")

    deserialized = codec.deserialize(serialized)
    print(f"BFS Deserialized matches root val: "
          f"{deserialized.val == root.val}")
