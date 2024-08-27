class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        @cache
        def dfs(i, j):
            #find distinct subsequence
            if j >= len(t):
                return 1
            #not find distinct subsequence
            if i >= len(s):
                return 0
            #compute distinct way for current index i, j
            ways = 0
            #one way
            if s[i] == t[j]:
                ways += dfs(i+1, j+1)
            #the other way
            ways += dfs(i+1,j)

            return ways

        return dfs(0,0)