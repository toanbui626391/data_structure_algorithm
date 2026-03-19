"""
Given an integer array nums, return all triplets
[nums[i], nums[j], nums[k]] such that i, j, k are
distinct and nums[i] + nums[j] + nums[k] == 0.
The solution set must not contain duplicate triplets.

Example:
  Input:  nums=[-1,0,1,2,-1,-4]
  Output: [[-1,-1,2],[-1,0,1]]
"""


def threeSum(nums: list[int]) -> list[list[int]]:
    result = []

    # Sorting enables two-pointer and duplicate skipping.
    nums.sort()

    for i in range(len(nums)):
        # Skip duplicate values for the outer element.
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            # Sum too large; shrink from the right.
            if current_sum > 0:
                right -= 1
            # Sum too small; grow from the left.
            elif current_sum < 0:
                left += 1
            else:
                result.append(
                    [nums[i], nums[left], nums[right]]
                )
                left += 1
                # Skip duplicate left values to avoid duplicates.
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

    return result
