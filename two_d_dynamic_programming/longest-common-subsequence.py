"""
Given two strings s and t, return the length of
their longest common subsequence.

Example:
  Input:  s="abcde", t="ace"
  Output: 3

Constraints:
  When characters match, extend; otherwise take the longer branch.
"""

from functools import cache


class Solution:
    def longestCommonSubsequence(
        self, s: str, t: str
    ) -> int:
        @cache
        def recurse(idx_s, idx_t):
            if idx_s < len(s) and idx_t < len(t):
                # Matching characters extend the subsequence by 1.
                if s[idx_s] == t[idx_t]:
                    return 1 + recurse(idx_s + 1, idx_t + 1)
                # Try advancing either string independently.
                return max(
                    recurse(idx_s, idx_t + 1),
                    recurse(idx_s + 1, idx_t),
                )
            return 0

        return recurse(0, 0)
