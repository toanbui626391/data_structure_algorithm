#problem understand:
    #An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
    #Given two strings s and t, return true if t is an anagram of s, and false otherwise.

#strategy to sole problem
    #two string is anagrams have to have the same length
    #approach one: two string anagrams will have the same number of character
    #approach two: 

#########################################reference solution
from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)
