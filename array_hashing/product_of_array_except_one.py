#problem understanding
    #Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]
    #You must write an algorithm that runs in O(n) time and without using the division operation.

#strategy to sole problem:
    #we have to know product of prefix and postfix
    #we need temp array to hold prefix and postfix and then compute product for each element

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []*len(nums)
        pre = 1
        post = 1
        for i in range(len(nums)):
            result[i] = pre
            pre = result[i] * pre
            result[len(nums) - 1] = post
            post = result[len(nums) - 1] * post
        return result