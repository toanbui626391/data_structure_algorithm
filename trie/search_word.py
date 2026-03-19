"""
Design a data structure that supports addWord and
search, where '.' in a search pattern matches any
single letter.

Example:
  addWord("bad"); addWord("dad"); addWord("mad")
  search("pad") -> False; search(".ad") -> True

Constraints:
  DFS through trie branches handles the '.' wildcard.
"""


class TrieNode:
    def __init__(self):
        # Map character to child TrieNode.
        self.children = {}
        self.word = False


class WordDictionary:
    def __init__(self):
        # Start with a single empty root node.
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.word = True

    def search(self, word: str) -> bool:
        def dfs(idx, root):
            curr = root

            for i in range(idx, len(word)):
                char = word[i]
                if char == ".":
                    # Try every existing child branch.
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]
            return curr.word

        return dfs(0, self.root)
