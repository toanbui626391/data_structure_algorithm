"""
Problem: Group Anagrams

Given an array of strings strs, group the
anagrams together. You can return the answer
in any order.

Example:
  Input:  strs=["eat","tea","tan","ate","nat","bat"]
  Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Approach: Hash Map with Sorting
  - Anagrams share the same characters.
  - Sorting a string gives a canonical version
    of that string ("eat" -> "aet", "tea" -> "aet").
  - Use a hash map where the key is the sorted
    string and the value is a list of anagrams.
"""

from typing import List

class Solution:
    def groupAnagrams(
        self, strs: List[str]
    ) -> List[List[str]]:
        
        # Maps sorted string -> list of anagrams
        anagram_map = {}
        
        for word in strs:
            # Sort the word to create the hash key
            sorted_word = "".join(sorted(word))
            
            if sorted_word not in anagram_map:
                anagram_map[sorted_word] = []
                
            anagram_map[sorted_word].append(word)
            
        return list(anagram_map.values())
