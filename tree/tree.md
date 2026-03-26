# Tree Data Structure

## What is a Tree?
A tree is a hierarchical data structure that
organizes nodes in a parent-child relationship.
Unlike a linked list (linear), a tree branches
out, like an upside-down tree in nature.

Key terminology:
* **Root:** The topmost node with no parent.
* **Leaf:** A node with no children.
* **Height:** Longest path from root to a leaf.
* **Depth:** Distance of a node from the root.
* **Subtree:** A node and all of its descendants.

The most common tree in interviews is the
**Binary Tree**, where each node has at most
two children: a left child and a right child.

A **Binary Search Tree (BST)** adds a rule:
* All nodes in the left subtree are smaller.
* All nodes in the right subtree are larger.

Standard node definition in Python:
```python
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
```

---

## Algorithms on Trees

### 1. Depth-First Search (DFS)
**Core idea:** Explore as far as possible down
one branch before backtracking. Implemented
naturally with recursion (the call stack acts
as the explicit stack).

There are three DFS orderings:
* **Pre-order:** root -> left -> right
* **In-order:** left -> root -> right
  * Visits BST nodes in sorted order!
* **Post-order:** left -> right -> root
  * Process children before the parent.

```python
# Pre-order: root, left, right
def preorder(root):
    if not root:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)


# In-order: left, root, right
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)


# Post-order: left, right, root
def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val)
```

---

### 2. Breadth-First Search (BFS)
**Core idea:** Visit all nodes level-by-level,
from top to bottom. Implemented with a queue
(collections.deque). BFS is the standard
approach for any "level order" problem.

```python
from collections import deque


def bfs(root):
    if not root:
        return
    queue = deque([root])

    while queue:
        # Process all nodes on the current level.
        for _ in range(len(queue)):
            node = queue.popleft()
            print(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
```

---

### 3. Tree Height / Max Depth
**Core idea:** Use post-order DFS. The height
of a node is 1 + the max height of its two
children. The base case (None) returns 0.

```python
def maxDepth(root):
    if not root:
        return 0
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    return 1 + max(left_depth, right_depth)
```

---

### 4. BST Insert and Search
**Core idea:** At each node in the BST, compare
the target value to the current node. Recurse
left if smaller, right if larger.

```python
# Search in BST: O(log n) avg, O(n) worst
def searchBST(root, val):
    if not root or root.val == val:
        return root
    if val < root.val:
        return searchBST(root.left, val)
    return searchBST(root.right, val)


# Insert into BST: O(log n) avg
def insertBST(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insertBST(root.left, val)
    else:
        root.right = insertBST(root.right, val)
    return root
```

---

### 5. Lowest Common Ancestor (LCA)
**Core idea:** Use DFS. If both target nodes
are in different subtrees (one left, one right),
the current node is their LCA. If both are in
the same subtree, recurse in that direction.

```python
def lowestCommonAncestor(root, p, q):
    if not root:
        return None

    # Found one of the targets.
    if root == p or root == q:
        return root

    left = lowestCommonAncestor(
        root.left, p, q
    )
    right = lowestCommonAncestor(
        root.right, p, q
    )

    # Targets are in different subtrees.
    if left and right:
        return root

    # Both targets are in the same subtree.
    return left if left else right
```

---

### 6. Check if a Tree is Balanced
**Core idea:** Use a post-order DFS that returns
the height of each subtree. If at any node the
height difference between left and right is more
than 1, the tree is unbalanced.

```python
def isBalanced(root):
    def dfs(node):
        # Returns -1 if unbalanced, else height.
        if not node:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)

        # Propagate the "unbalanced" signal up.
        if left == -1 or right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    return dfs(root) != -1
```

---

## Algorithm Comparison

- **DFS (recursive)**
  - Used for: path finding, height,
    subtree problems, LCA
  - Time: O(n), Space: O(h)
    (h = tree height, O(log n) balanced,
     O(n) worst case skewed)

- **BFS (queue)**
  - Used for: level-order traversal,
    shortest path in unweighted tree
  - Time: O(n), Space: O(w)
    (w = max width of tree)

- **BST Search/Insert**
  - Used for: ordered data with fast
    lookup and insertion
  - Time: O(log n) avg, O(n) worst
