"""
Problem: Contains Duplicate

Given an integer array nums, return true if any
value appears at least twice in the array, and
return false if every element is distinct.

Example:
  Input:  nums = [1,2,3,1]
  Output: True

Approach: Hash Set
  - Use a hash set to track seen numbers.
  - Set lookups are O(1) on average.
  - As we iterate, if a number is already in
    the set, we found a duplicate.
"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
            
        return False
