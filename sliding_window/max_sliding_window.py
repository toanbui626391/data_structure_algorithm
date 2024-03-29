
#strategy to solve the problem
    #goal: find max value in window with size k
    #why:
        #using sliding windows
        #using deque: 
            #to hold the index of the current window
            #to hold index of decreasing value of nums
        #the key idea:
            #to maintain maintain the decreasing que of index
            #for very right index remove index which have value smaller than right index
from typing import List
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()  # index
        l = r = 0
        # O(n) O(n)
        while r < len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left val from window
            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output
