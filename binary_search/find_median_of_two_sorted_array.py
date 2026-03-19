"""
Given two sorted arrays nums1 and nums2, return
the median of the two sorted arrays. The overall
run time complexity should be O(log(m+n)).

Example:
  Input:  nums1=[1,3], nums2=[2]
  Output: 2.0

Constraints:
  Binary search on the shorter array to find the partition.
"""

from typing import List


class Solution:
    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        length = len(nums1) + len(nums2)
        half = length // 2

        # Always binary search on the shorter array.
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        left, right = 0, len(nums1) - 1
        while True:
            # Partition indices for each array.
            i = (left + right) // 2
            j = half - i - 2

            nums1_left = (
                nums1[i] if i >= 0 else float("-infinity")
            )
            nums1_right = (
                nums1[i + 1]
                if (i + 1) < len(nums1)
                else float("infinity")
            )
            nums2_left = (
                nums2[j] if j >= 0 else float("-infinity")
            )
            nums2_right = (
                nums2[j + 1]
                if (j + 1) < len(nums2)
                else float("infinity")
            )

            # Correct partition found.
            if (
                nums1_left <= nums2_right
                and nums2_left <= nums1_right
            ):
                if length % 2:
                    return min(nums1_right, nums2_right)
                return (
                    max(nums1_left, nums2_left)
                    + min(nums1_right, nums2_right)
                ) / 2

            if nums1_left > nums2_right:
                right = i - 1
            else:
                left = i + 1
