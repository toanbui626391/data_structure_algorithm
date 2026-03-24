"""
Problem: 3Sum

Given an integer array nums, return all triplets
such that nums[i] + nums[j] + nums[k] == 0 with
distinct indices. No duplicate triplets allowed.

Example:
  Input:  nums=[-1,0,1,2,-1,-4]
  Output: [[-1,-1,2], [-1,0,1]]

Approach: Sorting + Two Pointers
  - Sort the array first.
  - Pin one number (anchor) and use two pointers
    (left and right) for the remaining array to
    find pairs that sum to -anchor.
  - Skip duplicates for both the anchor and the
    left pointer to avoid duplicate triplets.
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # If anchor is positive, sum can't be zero
            if a > 0:
                break
                
            # Skip duplicate anchors
            if i > 0 and a == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                three_sum = a + nums[left] + nums[right]
                
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    res.append([a, nums[left], nums[right]])
                    # Move left and bypass duplicates
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                        
        return res
