"""
Problem:
Given two strings s and t, return the length of
their longest common subsequence.

Examples:
Input: s = "abcde", t = "ace"
Output: 3

Constraints:
1 <= s.length, t.length <= 1000
"""

from functools import cache


class Solution:
    def longestCommonSubsequence(
        self, s: str, t: str
    ) -> int:
        @cache
        def recurse(idx_s, idx_t):
            if idx_s < len(s) and idx_t < len(t):
                # Matching chars extend sequence by 1.
                if s[idx_s] == t[idx_t]:
                    res = 1 + recurse(idx_s + 1, idx_t + 1)
                    return res
                
                # Try advancing either string.
                skip_s = recurse(idx_s + 1, idx_t)
                skip_t = recurse(idx_s, idx_t + 1)
                
                return max(skip_s, skip_t)
            
            return 0

        return recurse(0, 0)

    def longestCommonSubsequenceDP(
        self, s: str, t: str
    ) -> int:
        m = len(s)
        n = len(t)
        
        # Initialize (m+1) x (n+1) grid with zeros.
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Characters match, extend the sequence.
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    # No match, max of skipping either.
                    max_skip_s = dp[i - 1][j]
                    max_skip_t = dp[i][j - 1]
                    
                    dp[i][j] = max(max_skip_s, max_skip_t)
                    
        return dp[m][n]


if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1
    s1 = "abcde"
    t1 = "ace"
    
    res_dfs_1 = sol.longestCommonSubsequence(s1, t1)
    res_dp_1 = sol.longestCommonSubsequenceDP(s1, t1)
    
    print("Test 1 (s='abcde', t='ace'):")
    print(f"DFS output: {res_dfs_1}")
    print(f"DP output:  {res_dp_1}")
    print()
    
    # Test case 2
    s2 = "abc"
    t2 = "abc"
    
    res_dfs_2 = sol.longestCommonSubsequence(s2, t2)
    res_dp_2 = sol.longestCommonSubsequenceDP(s2, t2)
    
    print("Test 2 (s='abc', t='abc'):")
    print(f"DFS output: {res_dfs_2}")
    print(f"DP output:  {res_dp_2}")
    print()
    
    # Test case 3
    s3 = "abc"
    t3 = "def"
    
    res_dfs_3 = sol.longestCommonSubsequence(s3, t3)
    res_dp_3 = sol.longestCommonSubsequenceDP(s3, t3)
    
    print("Test 3 (s='abc', t='def'):")
    print(f"DFS output: {res_dfs_3}")
    print(f"DP output:  {res_dp_3}")
