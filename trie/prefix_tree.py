"""
Implement a trie (prefix tree) with insert, search,
and startsWith methods.

Example:
  insert("apple"); search("apple") -> True
  search("app") -> False; startsWith("app") -> True

Constraints:
  Each TrieNode has 26 children (one per lowercase letter).
"""


class TrieNode:
    def __init__(self):
        # 26 slots for lowercase letters; None means absent.
        self.children = [None] * 26
        self.end = False


class Trie:
    def __init__(self):
        """
        Initialize the trie with an empty root node.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for char in word:
            idx = ord(char) - ord("a")
            if curr.children[idx] is None:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.end = True

    def search(self, word: str) -> bool:
        """
        Returns True if the word is in the trie.
        """
        curr = self.root
        for char in word:
            idx = ord(char) - ord("a")
            if curr.children[idx] is None:
                return False
            curr = curr.children[idx]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns True if any word starts with prefix.
        """
        curr = self.root
        for char in prefix:
            idx = ord(char) - ord("a")
            if curr.children[idx] is None:
                return False
            curr = curr.children[idx]
        return True
