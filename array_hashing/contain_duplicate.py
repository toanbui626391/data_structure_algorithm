#problem understanding
    #Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

#strategy to solve problem
    #using set to keep track of element have seen before
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        collector = set()
        for e in nums:
            if e in collector:
                return True
            collector.add(e)
        return False