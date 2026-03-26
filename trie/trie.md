# Trie Data Structure

## What is a Trie?
A Trie (pronounced "try", from re**trie**val) is a
tree-like data structure designed for storing and
searching strings efficiently. Unlike a hash map
that stores complete words as keys, a Trie breaks
each word into individual characters and stores
each character as a node in the tree.

Each node typically contains:
* A map/dict of children (one per character).
* A boolean flag marking if this node is the
  end of a complete word.

A Trie with ["app", "apple", "api"]:
```
root
 └── a
      └── p
           ├── p (end=True)  -> "app"
           │    └── l
           │         └── e (end=True) -> "apple"
           └── i (end=True)  -> "api"
```

---

## Core Idea
The core idea is **shared prefix storage**. All
words that share a common prefix (e.g. "app" and
"apple") share the same path from the root. This
makes prefix-based queries extremely fast.

**When to use a Trie:**
* Autocomplete / typeahead search
* Spell-checking
* Prefix matching / IP routing
* Word search in a grid (with DFS)

---

## Standard Implementation

```python
class TrieNode:
    def __init__(self):
        # Map character -> TrieNode child
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Insert a word into the trie.
        Time: O(m), m = len(word)
        """
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        """
        Return True if the exact word exists.
        Time: O(m), m = len(word)
        """
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        """
        Return True if any word starts with prefix.
        Time: O(m), m = len(prefix)
        """
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True
```

---

## Core Operations

- **insert:** Walk down the trie one character
  at a time, creating new nodes as needed.
  Mark the final node as `is_end = True`.

- **search:** Walk down the trie. If any
  character is missing, return `False`. After
  the last character, return `is_end`.

- **startsWith:** Identical to `search` but
  does NOT check `is_end`. Any node reached
  at the end of the prefix means the prefix
  exists.

---

## Complexity Summary

- **Insert:** Time O(m), Space O(m)
- **Search:** Time O(m), Space O(1)
- **startsWith:** Time O(m), Space O(1)
- m = length of the word or prefix

The total space for N words with average
length m is O(N * m) in the worst case (no
shared prefixes). With many shared prefixes,
space is much smaller in practice.

---

## Common Problem Patterns

* **Prefix search / autocomplete**
  Use `startsWith` to filter candidates.

* **Word search in a grid**
  Combine a Trie with DFS on a 2D grid.
  The Trie prunes dead-end paths early.

* **Word dictionary with wildcards**
  Use DFS on the Trie where `.` means
  "try all children at this level."
