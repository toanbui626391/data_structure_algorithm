"""
Problem: Two Sum

Given an array of integers nums and an integer
target, return indices of the two numbers such
that they add up to target.
Exactly one solution exists; each element used once.

Example:
  Input:  nums=[2,7,11,15], target=9
  Output: [0,1]

Approach: Hash Map
  - Iterate through the array once.
  - Calculate `needed = target - current_value`.
  - Check if `needed` exists in our hash map.
  - If yes, return indices. Otherwise, store the
    current value and index into the map.
"""

from typing import List

class Solution:
    def twoSum(
        self, nums: List[int], target: int
    ) -> List[int]:
        
        # Map values to their indices
        seen = {}
        
        for i, val in enumerate(nums):
            needed = target - val
            
            if needed in seen:
                # Return the matching index first
                return [seen[needed], i]
                
            seen[val] = i
            
        return []
