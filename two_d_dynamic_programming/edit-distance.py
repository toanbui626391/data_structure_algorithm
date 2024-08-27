class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}
        
        def getResult(i,j):
            if i == len(word1) and j == len(word2):
                return 0
            if i == len(word1):  # Reached end of word1, Insert all left from word2
                return len(word2) - j
            if j == len(word2): # All chars of word2 are matched, Remove all left from word2
                return len(word1) - i

            if (i, j) not in dp:
                if word1[i] == word2[j]:
                    ans = getResult(i + 1, j + 1)
                else: 
                    insert = 1 + getResult(i, j + 1) #insert
                    delete = 1 + getResult(i + 1, j) #delete
                    replace = 1 + getResult(i + 1, j + 1) #replace
                    ans = min(insert, delete, replace)
                dp[(i, j)] = ans
            return dp[(i, j)]
        
        return getResult(0,0)