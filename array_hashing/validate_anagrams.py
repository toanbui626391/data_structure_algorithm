"""
Problem: Valid Anagram

Given two strings s and t, return true if t is
an anagram of s, and false otherwise.

Example:
  Input:  s="anagram", t="nagaram"
  Output: True

Approach: Hash Map Counting
  - If lengths differ, they can't be anagrams.
  - Count frequencies of chars in both strings.
  - Compare the frequency maps.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        count_s = {}
        count_t = {}
        
        for i in range(len(s)):
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_t[t[i]] = count_t.get(t[i], 0) + 1
            
        return count_s == count_t
