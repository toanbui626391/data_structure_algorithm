#problem understanding
    #Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]
    #You must write an algorithm that runs in O(n) time and without using the division operation.

#strategy to sole problem:
    #we have to know product of prefix and postfix
    #we need temp array to hold prefix and postfix and then compute product for each element
    #data structure:
        #pre (int): to hold pre product of each index
        #post (int): to hold post product of each index
        #res (list): each index position will hold value of pre*post
    #we have do the multiplication for each index by move point forward and backford as the same time

##################################################reference solution
from types import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length=len(nums)
        #build array to hold temp data and result
        sol=[1]*length
        pre = 1 #hold the current pre
        post = 1 #hodl the current post
        for i in range(length):
            sol[i] *= pre
            pre = pre*nums[i]
            sol[length-i-1] *= post
            post = post*nums[length-i-1]
        return(sol)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length=len(nums)
        #build array to hold temp data and result
        pre = [1] * length
        post = [1] * length
        value = 1
        for i in range(length):
            pre[i] *= value
            value *= nums[i] * value 

        value = 1
        for i in range(length - 1, 0, -1):
            post[i] *= value
            value = nums[i] * value


        for i in range(len(nums)):
            