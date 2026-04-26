"""
Problem:
Given an m x n grid, count unique paths from
the top-left to the bottom-right corner. You
may only move right or down.

Examples:
Input: m = 3, n = 7
Output: 28

Constraints:
1 <= m, n <= 100
"""

from functools import cache


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Count leaves (valid endpoints) in the tree.
        @cache
        def dfs(i, j):
            if (i, j) == (m - 1, n - 1):
                return 1
            
            if i >= m or j >= n:
                return 0
            
            # Move down or move right.
            paths_down = dfs(i + 1, j)
            paths_right = dfs(i, j + 1)
            
            return paths_down + paths_right

        return dfs(0, 0)

    def uniquePathsDP(self, m: int, n: int) -> int:
        # Create a 2D grid initialized to 1.
        # First row and column naturally have 1 path.
        dp = [[1] * n for _ in range(m)]

        # Iterate starting from (1, 1).
        for i in range(1, m):
            for j in range(1, n):
                # Sum paths from top and left.
                paths_top = dp[i - 1][j]
                paths_left = dp[i][j - 1]
                
                dp[i][j] = paths_top + paths_left

        # Return bottom-right corner value.
        return dp[m - 1][n - 1]


if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1
    m1 = 3
    n1 = 7
    
    res_dfs_1 = sol.uniquePaths(m1, n1)
    res_dp_1 = sol.uniquePathsDP(m1, n1)
    
    print("Test 1 (m=3, n=7):")
    print(f"DFS output: {res_dfs_1}")
    print(f"DP output:  {res_dp_1}")
    print()
    
    # Test case 2
    m2 = 3
    n2 = 2
    
    res_dfs_2 = sol.uniquePaths(m2, n2)
    res_dp_2 = sol.uniquePathsDP(m2, n2)
    
    print("Test 2 (m=3, n=2):")
    print(f"DFS output: {res_dfs_2}")
    print(f"DP output:  {res_dp_2}")
