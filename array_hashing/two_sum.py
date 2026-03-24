"""
Problem: Two Sum

Given an array of integers nums and an integer
target, return indices of the two numbers such
that they add up to target.

Example:
  Input:  nums=[2,7,11,15], target=9
  Output: [0,1]

Approach: Hash Map
  - Track seen values and their indices.
  - Calculate `complement = target - num`.
  - Check if `complement` is in our seen map.
"""

from typing import List


class Solution:
    def twoSum(
        self, nums: List[int], target: int
    ) -> List[int]:
        
        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in seen:
                return [seen[complement], i]
                
            seen[num] = i
            
        return []
