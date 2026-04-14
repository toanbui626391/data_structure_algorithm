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


# BFS approach: Kahn's Algorithm (topological sort)
# Key idea:
#   - Build a graph and in-degree count.
#   - Start BFS from nodes with in-degree 0.
#   - A cycle exists if not all nodes are visited.
class SolutionBFS:
    def alienOrder(self, words: list[str]) -> str:
        # Build adjacency set for every character.
        adj = {
            char: set()
            for word in words
            for char in word
        }

        # Compare adjacent word pairs to find edges.
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))

            # Longer word before its prefix = invalid.
            if (
                len(w1) > len(w2)
                and w1[:min_len] == w2[:min_len]
            ):
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        # Count in-degrees for each character.
        in_degree = {char: 0 for char in adj}
        for char in adj:
            for neighbor in adj[char]:
                in_degree[neighbor] += 1

        # Seed the queue with zero-in-degree nodes.
        from collections import deque
        queue = deque(
            [c for c in in_degree if in_degree[c] == 0]
        )
        result = []

        while queue:
            char = queue.popleft()
            result.append(char)

            for neighbor in adj[char]:
                in_degree[neighbor] -= 1
                # Add to queue when all predecessors
                # have been processed.
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # If result length != total unique chars,
        # a cycle exists → invalid ordering.
        if len(result) != len(in_degree):
            return ""

        return "".join(result)


if __name__ == "__main__":
    sol = SolutionBFS()

    # Example 1 → expected "wertf"
    words1 = ["wrt", "wrf", "er", "ett", "rftt"]
    print(sol.alienOrder(words1))

    # Example 2 → expected "z" or "zx"
    words2 = ["z", "x"]
    print(sol.alienOrder(words2))

    # Example 3 → invalid, expected ""
    words3 = ["z", "x", "z"]
    print(sol.alienOrder(words3))
