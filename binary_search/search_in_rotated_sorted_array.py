#understand the problem

#strategy to solve the problem
    #goal: search and return index of a target in a rotated sorted array

    #why:
        #it is a rotated sorted array. we do not know pivot point but we know there are two increase array.
        #using binary search to use above feature
        #for each num[mid] we have to know which portion of array we are in
        #when we know what portion of array we condition to find which way to go using binary search

        #the key is to know both target and mid are in which portion. and relative between mid and target
            #if target < nums[l]: target have to be in the right
            #if target > nums[r]: target have to be in the left

    #variable:
        #l, r (int): to do binary search and keep track of search area
        #mid (int): to keep the searching index
#########################################reference to solution
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            # left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1