# Trees Data Structure

## What Is It?

A **Tree** is a hierarchical, non-linear data
structure composed of **nodes**. It starts at
a root node and expands outward through
parent-child relationships.

Key terms:
- **Root:** The topmost node (no parent).
- **Leaf:** A node with no children.
- **Height:** The longest path from root to
  a leaf node.
- **Depth:** The distance from the root to
  a specific node.

### Standard Binary Tree Node (Python)
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

---

## Core Idea

The power of trees lies in their **recursive
structure**. Every subtree is itself a tree.
This means most tree algorithms can be expressed
as:

1. Do something at the current node.
2. Recursively do the same to the left child.
3. Recursively do the same to the right child.

For **Binary Search Trees (BST)**, the rule is:
all values in the left subtree are smaller than
the root, and all values in the right subtree
are greater — allowing O(log N) search.

---

## Core Algorithms

### 1. Depth-First Search (DFS)

DFS explores as far down a branch as possible
before backtracking. It is implemented via
recursion or an explicit stack.

There are three DFS ordering variants:

```python
# Pre-order: Root -> Left -> Right
def preorder(node):
    if not node:
        return
    print(node.val)   # process root FIRST
    preorder(node.left)
    preorder(node.right)

# In-order: Left -> Root -> Right
# (Yields sorted values for a BST)
def inorder(node):
    if not node:
        return
    inorder(node.left)
    print(node.val)   # process root MIDDLE
    inorder(node.right)

# Post-order: Left -> Right -> Root
# (Process children before parent)
def postorder(node):
    if not node:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.val)   # process root LAST
```

### 2. Breadth-First Search (BFS)

BFS visits all nodes level by level, from top
to bottom. It uses a queue, not a stack.

```python
from collections import deque

def bfs(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level = []
        # Process all nodes in this level
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)

    return result
```

### 3. BST Search and Insert

```python
def search(node, target):
    if not node:
        return False
    if node.val == target:
        return True
    if target < node.val:
        return search(node.left, target)
    return search(node.right, target)


def insert(node, val):
    if not node:
        return TreeNode(val)
    if val < node.val:
        node.left = insert(node.left, val)
    else:
        node.right = insert(node.right, val)
    return node
```

---

## Suitable Problem Types

### Path and Subtree Problems
- **Maximum Depth of Binary Tree:** DFS,
  return 1 + max(left depth, right depth).
- **Diameter of Binary Tree:** At each node,
  the diameter is left height + right height.
  Track the global max during DFS.
- **Path Sum:** DFS while subtracting the
  node's value from the target. Return True
  when hitting a leaf with target = 0.

### Tree Validation and Comparison
- **Validate BST:** DFS with a valid range
  `[min, max]`. Narrow the range at each step.
- **Same Tree / Symmetric Tree:** Recursive
  structural comparison of left and right
  subtrees.

### Level-Order / BFS Problems
- **Binary Tree Level Order Traversal:** BFS
  captures each level as a snapshot.
- **Right Side View:** BFS; record only the
  last node of each level.

### Lowest Common Ancestor
- **LCA of Two Nodes:** DFS through the tree.
  If one target is in the left subtree and the
  other is in the right, the current node is
  the LCA.

### BST-Specific Problems
- **Kth Smallest in BST:** In-order DFS
  naturally yields sorted values; return the
  Kth element.
- **Convert Sorted Array to BST:** Recursively
  pick the midpoint as the root to ensure the
  tree is balanced.

---

## Complexity

**For a balanced binary tree (height = log N):**
- **DFS / BFS:** O(N) time, O(H) space.
  - Where H = log N (balanced) or N (skewed).
- **BST Search / Insert:** O(log N) time.

**For a degenerate/skewed tree (height = N):**
- BST operations degrade to O(N) time (like
  a linked list).

This is why self-balancing trees like AVL or
Red-Black Trees maintain the O(log N) guarantee.
