"""
Given a string s, partition it so that every
substring in the partition is a palindrome.
Return all possible palindrome partitionings.

Example:
  Input:  s="aab"
  Output: [["a","a","b"],["aa","b"]]

Constraints:
  DFS with a palindrome check explores all valid cuts.
"""

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        part = []

        def dfs(idx):
            # Reached end; all parts are palindromes.
            if idx >= len(s):
                result.append(part[:])
                return
            for end_idx in range(idx, len(s)):
                if self.isPali(s, idx, end_idx):
                    part.append(s[idx: end_idx + 1])
                    dfs(end_idx + 1)
                    part.pop()

        dfs(0)
        return result

    def isPali(self, s, left, right):
        # Two-pointer palindrome check.
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
