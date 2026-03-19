"""
Given strings s and t, return the number of
distinct subsequences of s that equal t.

Example:
  Input:  s="rabbbit", t="rabbit"
  Output: 3

Constraints:
  Memoized DFS counts ways to match t[j:] using
  characters from s[i:], either skipping or
  consuming s[i] when it matches t[j].
"""

from functools import cache


class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        @cache
        def dfs(idx_s, idx_t):
            # Fully matched t: count this way.
            if idx_t >= len(t):
                return 1
            # Exhausted s without matching: dead end.
            if idx_s >= len(s):
                return 0

            ways = 0
            # Consume matching character from both.
            if s[idx_s] == t[idx_t]:
                ways += dfs(idx_s + 1, idx_t + 1)
            # Skip s[idx_s] and try next character.
            ways += dfs(idx_s + 1, idx_t)
            return ways

        return dfs(0, 0)
