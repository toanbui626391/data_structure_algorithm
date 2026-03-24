"""
Problem: Two Sum II (Input Array Is Sorted)

Given a 1-indexed sorted array numbers, find two
numbers that add up to target. Return their indices.
Exactly one solution exists.

Example:
  Input:  numbers=[2,7,11,15], target=9
  Output: [1,2]

Approach: Two Pointers (Converging)
  - Since the array is sorted, start pointers
    at both ends.
  - If sum > target, decrease right pointer to
    reduce the sum.
  - If sum < target, increase left pointer to
    increase the sum.
"""

from typing import List

class Solution:
    def twoSum(
        self, numbers: List[int], target: int
    ) -> List[int]:
        
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                # Problem requires 1-indexed array
                return [left + 1, right + 1]
                
            elif current_sum > target:
                right -= 1
                
            else:
                left += 1
                
        return []
