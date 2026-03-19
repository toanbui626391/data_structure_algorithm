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
