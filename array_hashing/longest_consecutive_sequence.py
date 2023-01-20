#problem understanding
    #Given an unsorted array of integers nums, 
    #return the length of the longest consecutive elements sequence.

#strategy to solve the problem
    #an element is head of sequece when e-1 not in set_collection
    #using set to reduce number of element we need to check
    #variable:
        #longest (int): to find the longest 
        #length (int): to find the length of current consecutive
        #set_nums (list[int]): to store unique element 

##################reference solution
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest = 0
        length = 0
        for e in set_nums:
            if e-1 not in set_nums: #check for head of sequence
                length = 1
                while e + length in set_nums: 
                    length += 1
            longest = max(length, longest)
        return longest