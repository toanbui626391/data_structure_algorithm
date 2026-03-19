"""
Given an array of integers nums and an integer
target, return indices of the two numbers such
that they add up to target.

You may assume that each input would have exactly
one solution, and you may not use the same element
twice. You can return the answer in any order.

Example:
  Input:  nums=[2,7,11,15], target=9
  Output: [0,1]

Example:
  Input:  nums=[3,2,4], target=6
  Output: [1,2]

Example:
  Input:  nums=[3,3], target=6
  Output: [0,1]
"""


def twoSum(nums: list[int], target: int) -> list[int]:
    # Store seen values and indices for O(1) lookup.
    seen = {}

    for i, num in enumerate(nums):
        # Calculate what complement is needed.
        complement = target - num

        # Return both indices if complement was seen.
        if complement in seen:
            return [seen[complement], i]

        # Record this number's index for future lookups.
        seen[num] = i

    # No valid pair found.
    return []
