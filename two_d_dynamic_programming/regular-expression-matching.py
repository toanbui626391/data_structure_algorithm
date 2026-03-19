"""
Given string s and pattern p, implement regular
expression matching with '.' (any char) and '*'
(zero or more of the preceding element).

Example:
  Input:  s="aa", p="a*"
  Output: True

Constraints:
  Memoized DFS on (i, j) indices; '*' requires
  checking both zero-use and one-use branches.
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dfs(idx_s, idx_p):
            if (idx_s, idx_p) in memo:
                return memo[(idx_s, idx_p)]

            # Both exhausted: full match.
            if idx_s >= len(s) and idx_p >= len(p):
                return True
            # Pattern exhausted but string remains.
            if idx_p >= len(p):
                return False

            # Current chars match if equal or '.'.
            same = idx_s < len(s) and (
                s[idx_s] == p[idx_p] or p[idx_p] == "."
            )

            # Look-ahead for '*' wildcard.
            if (
                (idx_p + 1) < len(p)
                and p[idx_p + 1] == "*"
            ):
                # Zero occurrences or one occurrence.
                result = dfs(idx_s, idx_p + 2) or (
                    same and dfs(idx_s + 1, idx_p)
                )
                memo[(idx_s, idx_p)] = result
                return result

            if same:
                result = dfs(idx_s + 1, idx_p + 1)
                memo[(idx_s, idx_p)] = result
                return result

            memo[(idx_s, idx_p)] = False
            return False

        return dfs(0, 0)
