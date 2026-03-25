"""
Problem: Find Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2, return
the median of the two sorted arrays. The overall
run time complexity should be O(log(min(m,n))).

Example:
  Input:  nums1=[1,3], nums2=[2]
  Output: 2.0

Approach: Binary Search on Partition
  - We want to partition both arrays such that
    the left halves contain exactly half the total
    elements, and every element in the left halves
    is <= every element in the right halves.
"""

from typing import List


class Solution:
    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        
        # Always binary search on the shorter array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        total_len = len(nums1) + len(nums2)
        half_len = total_len // 2

        left, right = 0, len(nums1) - 1
        
        while True:
            # i is partition in nums1, j in nums2
            i = left + (right - left) // 2
            j = half_len - i - 2

            # Edge cases: -inf out of bounds left,
            # inf out of bounds right
            A_left = nums1[i] if i >= 0 else float("-inf")
            A_right = (nums1[i + 1] if (i + 1) < len(nums1) 
                       else float("inf"))
                       
            B_left = nums2[j] if j >= 0 else float("-inf")
            B_right = (nums2[j + 1] if (j + 1) < len(nums2) 
                       else float("inf"))

            # Check if partition is correct
            if A_left <= B_right and B_left <= A_right:
                # Odd total length
                if total_len % 2 == 1:
                    return float(min(A_right, B_right))
                # Even total length
                return (max(A_left, B_left) + 
                        min(A_right, B_right)) / 2.0
                        
            elif A_left > B_right:
                # Move partition i left
                right = i - 1
            else:
                # Move partition i right
                left = i + 1
