#problem understanding
    #Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

#strategy to solve problem:
    #custom to this problem to two sum with two pointer
    #variables:
        #res (list of list): to store result is each element is list of 3 and unique
        # we have to sort nums in ascending order to solve this problem 
        #condition to stop seach for a the outer loop: if a > 0. because sum of three is 0 therefore it have to have at least one number smaller than 0
        #condition to check for the current a position is duplicate. if i >0 and nums[i - 1] = nums[i]
        #condition to check for duplicate in position b. while l < r and nums[l] == nums
#strategy to solve the problem
    #key one: sort nums list because we want to move three sum problem into two sum with sorted array
    #key two: nums contains duplicate element but return must not contain duplicate triplelet

    #variable:
        # res (list): to store a list of result
########################################reference solution
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # Skip positive integers
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res