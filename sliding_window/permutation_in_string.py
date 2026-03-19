"""
Given strings s1 and s2, return true if s2 contains
a permutation of s1. A permutation appears as a
contiguous substring of s2 with the same characters.

Example:
  Input:  s1="ab", s2="eidbaooo"
  Output: True

Constraints:
  Slide a fixed-width window and track character match counts.
"""

from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        # Count in reverse from s1; zero means that char is matched.
        counter = Counter(s1)
        matched = 0
        counter_len = len(counter)
        len_s1 = len(s1)

        for r in range(len(s2)):
            if s2[r] in counter:
                counter[s2[r]] -= 1
                if counter[s2[r]] == 0:
                    matched += 1

            # Slide the window by removing the leftmost character.
            if r >= len_s1 and s2[r - len_s1] in counter:
                if counter[s2[r - len_s1]] == 0:
                    matched -= 1
                counter[s2[r - len_s1]] += 1

            if matched == counter_len:
                return True

        return False
