"""
Given beginWord, endWord, and wordList, find the
length of the shortest transformation sequence
from beginWord to endWord, where each step changes
exactly one letter and the result must be in wordList.

Example:
  Input:  beginWord="hit", endWord="cog",
          wordList=["hot","dot","dog","lot","log","cog"]
  Output: 5

Constraints:
  BFS finds shortest paths; adjacency list on word patterns speeds lookups.
"""

import collections
from typing import List


class Solution:
    def ladderLength(
        self,
        beginWord: str,
        endWord: str,
        wordList: List[str],
    ) -> int:
        # The end word must be reachable.
        if endWord not in wordList:
            return 0

        # Build adjacency list keyed by wildcard patterns.
        neighbors = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for pos in range(len(word)):
                pattern = word[:pos] + "*" + word[pos + 1:]
                neighbors[pattern].append(word)

        visited = set([beginWord])
        queue = collections.deque([beginWord])
        result = 1
        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return result
                # Explore all one-letter-different neighbors.
                for pos in range(len(word)):
                    pattern = word[:pos] + "*" + word[pos + 1:]
                    for neighbor_word in neighbors[pattern]:
                        if neighbor_word not in visited:
                            visited.add(neighbor_word)
                            queue.append(neighbor_word)
            result += 1
        return 0
