#problem understanding:
    #

#strategy to solve the problem:
    #because it is two sum. therefore we given the index we know the value of the second value
    #variable:
        #keeper (dict): to keep track of key-paire (value:index). which value have seen before.
        #if we have compute the second value which have meet before return index of that value
##################################################reference solution
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        keeper = {}
        for i, v in enumerate(nums):
            value = target - v
            if value in keeper:
                return [i, keeper[value]]
            keeper[v] = i #keep track of value and index have meet before