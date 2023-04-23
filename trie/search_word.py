"""
strategy to solve the problem
    problem:
        design class which can addWord and search work efficient
    why:
        using Trie which each node is TrieNode
"""
class TrieNode:
    def __init__(self):
        self.children = {}  # a : TrieNode
        self.word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode() #init Trie with root TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root #start with root
        for c in word: #traverse to buld Trie
            if c not in cur.children: #if do not have TrieNode build it
                cur.children[c] = TrieNode()
            cur = cur.children[c] #move to next node
        cur.word = True #mark end of word

    def search(self, word: str) -> bool:
        def dfs(j, root): #
            cur = root #start search from root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word

        return dfs(0, self.root)
