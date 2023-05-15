"""
strategy to solve the problem
    problem:
        given a beginWord, endWord and wordList. find the shortest tranformtion path from befinWord to endWord
    why:
        using bfs() because we want to it find depth of the tree or graph faster than dfs
"""
import collections
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #check is the path possible. endWord have to be ben the list
        if endWord not in wordList:
            return 0
        #build ajaciency list to present graph. {pattern: [neighborWords, ]} because we want to visit node which valid operation
        nei = collections.defaultdict(list)
        wordList.append(beginWord) #beginWord is not in the list
        for word in wordList:
            for j in range(len(word)): #the length of word is much smaller compare to the length of words in list
                pattern = word[:j] + "*" + word[j + 1 :]
                nei[pattern].append(word)

        #using bfs
        visit = set([beginWord]) #only visit node one
        q = deque([beginWord]) #init que
        res = 1 #init result
        while q:
            for i in range(len(q)): #process work cat the current que
                word = q.popleft()
                if word == endWord:
                    return res
                #from current node word move to next child.
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1 :]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1 #update layer of graph
        return 0
