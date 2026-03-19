"""
Design a Least Recently Used (LRU) cache with O(1)
get and put operations.

Example:
  LRUCache(2); put(1,1); put(2,2); get(1)->1;
  put(3,3) evicts key 2; get(2)->-1.

Constraints:
  A doubly-linked list with a hash map achieves O(1) for both.
"""


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        # Maps key to its corresponding doubly-linked node.
        self.cache = {}

        # Sentinel left=LRU end, right=MRU end.
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        # Unlink node from its current position.
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        # Insert node just before the right sentinel (MRU).
        prev = self.right.prev
        nxt = self.right
        prev.next = nxt.prev = node
        node.next = nxt
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # Move accessed node to most-recent position.
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # Evict the LRU node when capacity is exceeded.
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
