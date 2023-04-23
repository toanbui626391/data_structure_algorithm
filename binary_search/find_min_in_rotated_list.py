#problem understanding

#strategy to solve the problem:
    #why:
        #because it is a sorted array and rorated therefore we can use binary search
        #at the rotate point nums[l] > num[r]
        #every element in left of pivot point will larger than every elemnt in right of pivot point
        #inside the section nums[l] < numpr

        #the key is to compare the middle position value to the most left position
    #variables:

########################################reference to solve the problem
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) -1
        res = nums[-1]
        while l <= r:
            mid = (l+r)//2
            if nums[mid] > nums[-1]: #mid in higher section
                l = mid + 1
            else: #mid in lower section
                r = mid - 1
                res = min(res, nums[mid])
        return res


class Solution:
    def findMin(self, nums: List[int]) -> int:
        start , end = 0 ,len(nums) - 1 
        curr_min = float("inf")
        
        while start  <  end :
            mid = (start + end ) // 2
            curr_min = min(curr_min,nums[mid])
            
            # right has the min 
            if nums[mid] > nums[end]:
                start = mid + 1
                
            # left has the  min 
            else:
                end = mid - 1 
                
        return min(curr_min,nums[start])