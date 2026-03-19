"""
Given a string s and an integer k, return the
length of the longest substring containing the
same letter after performing at most k replacements.

Example:
  Input:  s="ABAB", k=2
  Output: 4

Constraints:
  Window is valid when (size - max_char_count) <= k.
"""

from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_counter = Counter()
        left = 0
        result = 0
        # Track max frequency to avoid recomputing it each step.
        max_char = 0
        for r in range(len(s)):
            char_counter[s[r]] += 1
            max_char = max(max_char, char_counter[s[r]])
            total_char = r - left + 1
            # Shrink window when replacements needed exceed k.
            if total_char - max_char > k:
                char_counter[s[left]] -= 1
                left += 1
            else:
                result = max(result, total_char)
        return result
