#problem understanding
    #You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i])
    #Find two lines that together with the x-axis form a container, such that the container contains the most water.
    #Return the maximum amount of water a container can store.

#strategy to solve the problem:
    #brute force solution: O(n^2) two inner loop to check all combination
    #two pointer solution: O(n)
        #area = (r-l) * min(height[l], height[r])
        #we want maximum posible of (r-l)
        #we want to check all position solution of max height[l] and height[r]. Therefore:
            # if height[l] >= height[r]: #check combination of max height left
                # r += 1
            # else: #check combination of max height right
                # l -= 1
            #therefore, we can reduce number of operation to check to O(n)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height:
            return 0

        max_area = 0
        l, r = 0, len(height) - 1
        while l < r:
            max_area = max(max_area, (r-l)*min(height[l], height[r]))
            if height[l] >= height[r]:
                r -= 1
            else:
                l += 1
        return max_area