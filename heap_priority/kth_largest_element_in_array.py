"""
Given an integer array nums and integer k, return
the kth largest element in the array.

Example:
  Input:  nums=[3,2,1,5,6,4], k=2
  Output: 5

Constraints:
  QuickSelect finds the answer in O(n) average time.
"""

from typing import List


class Solution:
    def partition(
        self, nums: List[int], left: int, right: int
    ) -> int:
        # Use the rightmost element as pivot.
        pivot = nums[right]
        fill = left
        for i in range(left, right):
            if nums[i] <= pivot:
                nums[fill], nums[i] = nums[i], nums[fill]
                fill += 1
        # Place pivot in its sorted position.
        nums[fill], nums[right] = nums[right], nums[fill]
        return fill

    def findKthLargest(
        self, nums: List[int], k: int
    ) -> int:
        # Convert kth largest to the (len-k)th smallest index.
        target_index = len(nums) - k
        left, right = 0, len(nums) - 1
        while left < right:
            pivot_index = self.partition(nums, left, right)
            if pivot_index < target_index:
                left = pivot_index + 1
            elif pivot_index > target_index:
                right = pivot_index - 1
            else:
                break
        return nums[target_index]
