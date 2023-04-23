"""
strategy to solve the problem:
    #design Node: a note need key, val, prev (previous node) and next (next node)
        #why a node need to know it prev and next
            #with doubly linked list, we can move forward and backword
    #design LRUCache:
        #cap (capacity) (int): how many node we should have
        #cache (dict): map key with node
        #left (least recent use)
        #right (most recent)

        #why do we need remove and insert helper function
            #remove and update is to update the most recent use
    
    #remove note from doubly linked list
        #find prev, nxt node
        # change doubly linked list as follow: prev.next, nxt.prev = nxt, prev
    #insert node to the right
        find prev, nxt = self.right.prev, self.right
        #add double linked list for node. node.prev, node.next = prev, nxt
        #change linked list for prev and nex. prev.next = nxt.prev = node
    #put
        #if key in cache remove node. we have to create and add new node to cache 
        #after add new node to cache, check for key len if over capacity remove lru node
    #error notes:
        #we usaully wrong at put
            #when remove lru from doubly linked list, we also have to delete that from hash map
"""

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to node

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert node at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from the list and delete the LRU from hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]