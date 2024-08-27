class Solution:
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        #compute the length of their longest common subsequence
        #compute the max depth of the tree
        @cache
        def f(i, j):
            #add the depth of 1 when current char is the same and move to next char
            if i < len(s) and j < len(t):
                if s[i] == t[j]:
                    return 1 + f(i+1, j+1)
                #move right -> check next char of t, move down to check next char of s
                return max(f(i, j+1), f(i+1, j))
            #everything else do not have commem subsequence
            return 0
        
        return f(0, 0)