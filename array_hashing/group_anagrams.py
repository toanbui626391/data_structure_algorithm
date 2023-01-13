#problem understanding
    #Given an array of strings strs,
    #group the anagrams together.
    #You can return the answer in any order

#strategy to solve problem:
    #anagrams will have same set of character
        #counter of  anagrams will be the same
        #sorted anagrams will be the same
    #collector (defaultdict(list)) to collect element which is anagrams
        #key: is stored anagram
        #value: is list of anagrams
    #defaultdict(list) is a good data structure to collect value base on key because it return default empty list
    #how to build sorted string
###################################reference solution
from collections import defaultdict
from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        collector = defaultdict(list)
        for e in strs:
            value = "".join(sorted(e))
            collector[value].append(e)
        return collector.values()