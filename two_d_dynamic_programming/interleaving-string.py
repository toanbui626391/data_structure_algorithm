"""
Given strings s1, s2, and s3, determine if s3
is formed by interleaving s1 and s2.

Example:
  Input:  s1="aab", s2="axy",
          s3="aaxaby"
  Output: True

Constraints:
  Memoized DFS tracks indices into s1 and s2,
  checking if characters match s3 at position
  i+j.
"""

from functools import cache


class Solution:
    def isInterleave(
        self, s1: str, s2: str, s3: str
    ) -> bool:
        # Lengths must sum for interleaving to work.
        if len(s1) + len(s2) != len(s3):
            return False

        @cache
        def solve(idx1, idx2):
            # Both strings fully consumed: success.
            if idx1 == len(s1) and idx2 == len(s2):
                return True
            # Try advancing through s1.
            if (
                idx1 < len(s1)
                and s3[idx1 + idx2] == s1[idx1]
                and solve(idx1 + 1, idx2)
            ):
                return True
            # Try advancing through s2.
            if (
                idx2 < len(s2)
                and s3[idx1 + idx2] == s2[idx2]
                and solve(idx1, idx2 + 1)
            ):
                return True
            return False

        return solve(0, 0)

    def isInterleave(s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
            
        # Initialize DP table with False
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    # Can only come from the left (s2)
                    dp[i][j] = dp[i][j-1] and s2[j-1] == s3[i+j-1]
                elif j == 0:
                    # Can only come from above (s1)
                    dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i+j-1]
                else:
                    # Can come from either s1 or s2
                    from_s1 = dp[i-1][j] and s1[i-1] == s3[i+j-1]
                    from_s2 = dp[i][j-1] and s2[j-1] == s3[i+j-1]
                    dp[i][j] = from_s1 or from_s2
                    
        return dp[len(s1)][len(s2)]    
    
    
