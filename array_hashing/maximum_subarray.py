"""
Given an integer array nums, return the subarray
with the largest sum, and return its sum.

A subarray is a contiguous non-empty sequence
of elements within an array.

Example 1:
  Input:  nums=[-2,1,-3,4,-1,2,1,-5,4]
  Output: 6
  Explanation: [4,-1,2,1] has the largest sum.

Example 2:
  Input:  nums=[1]
  Output: 1

Example 3:
  Input:  nums=[5,4,-1,7,8]
  Output: 23

Constraints:
  1 <= nums.length <= 100,000
  -10,000 <= nums[i] <= 10,000
"""


def maxSubArray(nums: list[int]) -> int:
    # Kadane's algorithm: extend the current window
    # or start fresh when the running sum goes
    # negative.
    current_sum = nums[0]
    best_sum = nums[0]

    for num in nums[1:]:
        # A negative running sum hurts future windows;
        # reset to just this element.
        if current_sum < 0:
            current_sum = num
        else:
            current_sum += num

        # Track the best sum seen so far.
        if current_sum > best_sum:
            best_sum = current_sum

    return best_sum


if __name__ == "__main__":
    case_one = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # Expected: 6
    print(maxSubArray(case_one))

    case_two = [1]
    # Expected: 1
    print(maxSubArray(case_two))

    case_three = [5, 4, -1, 7, 8]
    # Expected: 23
    print(maxSubArray(case_three))
