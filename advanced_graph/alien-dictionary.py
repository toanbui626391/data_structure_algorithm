"""
Given a sorted list of words from an alien language,
derive the order of letters in the alien alphabet.
Return the order as a string, or "" if invalid.

Example:
  Input:  words=["wrt","wrf","er","ett","rftt"]
  Output: "wertf"

Constraints:
  Build a DAG from adjacent word pairs; topological sort gives the order.
"""


class Solution(object):
    def alienOrder(self, words):
        # Build adjacency set for each character found in words.
        adj = {char: set() for word in words for char in word}

        word_count = len(words)
        for i in range(word_count - 1):
            word1 = words[i]
            word2 = words[i + 1]
            min_len = min(len(word1), len(word2))
            # A longer word before its prefix is invalid.
            if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
                return ""
            for pos in range(min_len):
                if word1[pos] != word2[pos]:
                    adj[word1[pos]].add(word2[pos])
                    break

        # visited: True = currently on path, False = fully explored.
        visited = {}
        result = []

        def dfs(char):
            # A cycle is detected if we revisit a path node.
            if char in visited:
                return visited[char]
            visited[char] = True

            for neighbor in adj[char]:
                if dfs(neighbor):
                    return True
            # Mark as fully explored; add leaf nodes first.
            visited[char] = False
            result.append(char)

        for char in adj:
            if dfs(char):
                return ""
        # Reverse because DFS appends leaves first.
        return "".join(result[::-1])
