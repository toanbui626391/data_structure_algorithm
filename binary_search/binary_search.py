"""
strategy to solve the problem
    #why:
        #because this is a sorted list, we can use binary search to find target numser in the list
        #binary search:
            #start search from left and right
            #compare middle with target and update left or right.
    #variables:
        l, r (int): left, right index for search
        mid (int): to compare with target
    #error notes:
        condition to stop search when you have search all position. while l <= r

"""
"""
binary search:
    #to find item in a sorted array in O(logn) time.
    #start with left, right. left at from and right at end. l, r = 0, len(nums) - 1
    # compare middle index value with target to decide which portion of array possible target is in.
    #update l, r base on mid base on previous condition

"""
#################################reference solution
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)  # (l + r) // 2 can lead to overflow
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1