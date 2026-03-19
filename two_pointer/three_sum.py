"""
Given an integer array nums, return all triplets
such that nums[i] + nums[j] + nums[k] == 0 with
distinct indices. No duplicate triplets allowed.

Example:
  Input:  nums=[-1,0,1,2,-1,-4]
  Output: [[-1,-1,2],[-1,0,1]]

Constraints:
  Sort first to allow two-pointer on the inner pair.
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        # Sorting enables two-pointer and duplicate skipping.
        nums.sort()

        for i, anchor in enumerate(nums):
            # No valid triplet if anchor is positive.
            if anchor > 0:
                break
            # Skip duplicate anchor values.
            if i > 0 and anchor == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                triple_sum = anchor + nums[left] + nums[right]
                if triple_sum > 0:
                    right -= 1
                elif triple_sum < 0:
                    left += 1
                else:
                    result.append([anchor, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Skip duplicate left values.
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return result
