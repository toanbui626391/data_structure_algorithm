"""
An Anagram is a word or phrase formed by
rearranging the letters of a different word or
phrase, using all original letters exactly once.
Given two strings s and t, return true if t is
an anagram of s, and false otherwise.

Example:
  Input:  s="anagram", t="nagaram"
  Output: True

Constraints:
  Two anagrams must have the same length.
"""

from collections import Counter


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Length mismatch means they cannot be anagrams.
        if len(s) != len(t):
            return False
        # Same character counts confirm anagram relationship.
        return Counter(s) == Counter(t)
