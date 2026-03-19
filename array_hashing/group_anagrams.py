"""
Given an array of strings strs, group the
anagrams together. You can return the answer
in any order.

Example:
  Input:  strs=["eat","tea","tan","ate","nat","bat"]
  Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Constraints:
  Anagrams share the same sorted character sequence.
"""

from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # defaultdict(list) avoids KeyError on first access.
        collector = defaultdict(list)
        for element in strs:
            # Sorting produces a canonical key for all anagrams.
            key = "".join(sorted(element))
            collector[key].append(element)
        return collector.values()
