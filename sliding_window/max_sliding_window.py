"""
Problem: Maximum Sliding Window

Given an array nums and an integer k, return the
maximum value in each sliding window of size k.

Example:
  Input:  nums=[1,3,-1,-3,5,3,6,7], k=3
  Output: [3,3,5,5,6,7]

Approach: Monotonically Decreasing Deque
  - Maintain a deque of indices.
  - Keep the values corresponding to these
    indices strictly decreasing.
  - The front of the deque will always store
    the maximum for the current window.
  - Pop smaller elements from the back as new
    elements arrive.
  - Pop elements from the front when they fall
    outside the window boundary.
"""

from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(
        self, nums: List[int], k: int
    ) -> List[int]:
        
        output = []
        # Store indices of the array elements
        q = deque()
        
        for right in range(len(nums)):
            
            # 1. Pop from back: remove elements
            # smaller than the incoming element.
            while q and nums[q[-1]] < nums[right]:
                q.pop()
                
            # 2. Push to back: add incoming element
            q.append(right)
            
            # 3. Pop from front: remove if the left
            # boundary of window has passed the index
            left = right - k + 1
            if left > q[0]:
                q.popleft()
                
            # 4. Fetch the answer: when the first
            # full window size k is reached
            if right + 1 >= k:
                output.append(nums[q[0]])
                
        return output


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
    # Expected: [3, 3, 5, 5, 6, 7]
    
    print(sol.maxSlidingWindow([1], 1))
    # Expected: [1]
