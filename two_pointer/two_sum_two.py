#problem understanding:
    #Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order
    #ind two numbers such that they add up to a specific target number

#strategy to solve the problem:
    #because we know numbers is ascending order. Therefore we can use two pointer strategy to check where to move l or r
    #variable:
        # l, r (int): to keep track of position of left and right in numbers
        # total (int): numbers[l] + numbers[r]. because we need to use this value in multiple test

######################################reference solution
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) -1
        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l+1, r+1]
            if total > target:
                r -= 1
            if total < target:
                l += 1