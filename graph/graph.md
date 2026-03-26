# Graph Data Structure

## What is a Graph?
A graph is a data structure made up of:
* **Nodes (vertices):** The entities.
* **Edges:** Connections between nodes.

Unlike a tree, a graph can have:
* **Cycles** (paths that loop back).
* **Disconnected components** (islands of
  nodes with no path between them).
* **Directed edges** (one-way connections).
* **Weighted edges** (edges with a cost).

Common representations:
```python
# Adjacency List (most common in interviews)
# graph[node] = list of its neighbors
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1],
}

# Edge List
edges = [(0, 1), (0, 2), (1, 3)]
```

---

## Algorithm 1: DFS (Depth-First Search)
**Core idea:** Explore as far as possible
down one path before backtracking. Use a
`visited` set to avoid infinite loops in
graphs with cycles.

**Use for:** Connected components, cycle
detection, path existence, topological sort.

```python
def dfs(graph, node, visited):
    if node in visited:
        return
    visited.add(node)
    print(node)

    for neighbor in graph[node]:
        dfs(graph, neighbor, visited)


# Driver: handle disconnected graphs
def dfs_all(graph):
    visited = set()
    for node in graph:
        if node not in visited:
            dfs(graph, node, visited)
```

---

## Algorithm 2: BFS (Breadth-First Search)
**Core idea:** Explore all neighbors of the
current node before moving deeper. Use a
queue. BFS guarantees the **shortest path**
in an unweighted graph.

**Use for:** Shortest path in unweighted
graphs, level-order traversal, multi-source
BFS (e.g. rotting oranges).

```python
from collections import deque


def bfs(graph, start):
    visited = set([start])
    queue = deque([start])

    while queue:
        node = queue.popleft()
        print(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

---

## Algorithm 3: Topological Sort
**Core idea:** For a Directed Acyclic Graph
(DAG), produce an ordering where every node
comes before the nodes it points to.

Use post-order DFS: after visiting all
neighbors of a node, push it to a stack.
Reverse the stack at the end.

**Use for:** Course prerequisites, build
dependencies, task scheduling.

```python
def topo_sort(graph):
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        # Push after all neighbors visited.
        stack.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    # Reverse gives topological order.
    return stack[::-1]
```

---

## Algorithm 4: Union-Find (Disjoint Set)
**Core idea:** Track which nodes belong to
the same connected component. Two key ops:
* **find(x):** Return the root of x's group.
* **union(x, y):** Merge the two groups.

Path compression and union by rank make both
operations nearly O(1) amortized.

**Use for:** Detecting cycles, grouping
connected components, Kruskal's MST.

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        # Path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(
                self.parent[x]
            )
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False  # Already connected
        # Union by rank
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True
```

---

## Algorithm 5: Dijkstra's Shortest Path
**Core idea:** Find the shortest path from a
source node to all others in a **weighted**
graph with non-negative edges. Uses a
min-heap to always process the nearest
unvisited node next.

**Use for:** Shortest path in weighted graphs,
network routing, GPS navigation.

```python
import heapq


def dijkstra(graph, src):
    # graph[u] = list of (weight, v)
    dist = {node: float("inf") for node in graph}
    dist[src] = 0
    heap = [(0, src)]

    while heap:
        d, u = heapq.heappop(heap)

        # Skip if we found a better path already.
        if d > dist[u]:
            continue

        for weight, v in graph[u]:
            new_dist = dist[u] + weight
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(
                    heap, (new_dist, v)
                )
    return dist
```

---

## Algorithm Comparison

- **DFS**
  - Unweighted, path/cycle detection
  - Time O(V + E), Space O(V)

- **BFS**
  - Shortest path in unweighted graph
  - Time O(V + E), Space O(V)

- **Topological Sort**
  - Ordering for DAGs
  - Time O(V + E), Space O(V)

- **Union-Find**
  - Connected components, cycle detection
  - Time O(α(V)) per op ≈ O(1)

- **Dijkstra**
  - Shortest path in weighted graph
  - Time O((V + E) log V), Space O(V)

V = number of vertices, E = number of edges
