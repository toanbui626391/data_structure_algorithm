"""
Given a string s and a dictionary wordDict, return
true if s can be segmented into a space-separated
sequence of dictionary words.

Example:
  Input:  s="leetcode", wordDict=["leet","code"]
  Output: True

Constraints:
  dp[i] = True if s[0:i] can be segmented from the dictionary.
"""

from typing import List
from functools import cache


class Solution:
    def wordBreak(
        self, s: str, wordDict: List[str]
    ) -> bool:
        # dp[i] means the first i characters can be word-broken.
        dp = [True] + [False] * len(s)

        for end_idx in range(1, len(s) + 1):
            for start_idx in range(end_idx + 1):
                # Check if the left part is valid and right word exists.
                if dp[start_idx] and s[start_idx:end_idx] in wordDict:
                    dp[end_idx] = True
        return dp[-1]
