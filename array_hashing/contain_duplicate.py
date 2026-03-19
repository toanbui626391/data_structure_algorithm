"""
Given an integer array nums, return true if any
value appears at least twice in the array, and
return false if every element is distinct.
"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Use a set for O(1) average lookup time.
        collector = set()
        for element in nums:
            if element in collector:
                return True
            collector.add(element)
        return False
