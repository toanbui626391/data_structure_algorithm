#problem understanding
    #Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
    #return the maximum amount of water can be trap
#strategy to solve the problem
    #using two pointer strategy. We can use two pointer strategy because min(maxLeft, maxRigt) because if MaxLeft < MaxRight then min(maxLeft, maxRight)
    #variable:
        #l, r (int) is the pointer for left and right index heights
        #res (int) to store result of 
        #leftMax, rightMax (int): to store the max height of left and rigt position of the current position
        #res = max(leftMax, heights[i]) - height to avoide negative res
        #res[i] = min(maxLeft, maxRight) - heights[i]
            #maxLeft < maxRight => move left pointer

#strategy to solve the problem v2:
    #find max area using check all combination need O(n^2).
    #using two pointer instead we will check all position solution given that we want largest width position.
        #therefore,we only need to loop throug
#########################################reference code
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res