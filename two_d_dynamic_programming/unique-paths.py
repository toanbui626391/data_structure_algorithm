class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #compute number of possible unique path -> compute number of leaf
        @cache
        def dfs(i, j):
            if (i, j) == (m-1, n-1):
                return 1
            elif i >= m or j >= n:
                return 0
            #dfs(i+1, j) -> move down, dfs(i, j+1) move right
            return dfs(i+1, j) + dfs(i, j+1)
        return dfs(0, 0)
        