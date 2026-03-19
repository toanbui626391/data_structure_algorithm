"""
Given an array nums and an integer k, return the
maximum value in each sliding window of size k.

Example:
  Input:  nums=[1,3,-1,-3,5,3,6,7], k=3
  Output: [3,3,5,5,6,7]

Constraints:
  A monotonic deque maintains the window maximum in O(1).
"""

from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(
        self, nums: List[int], k: int
    ) -> List[int]:
        output = []
        # Deque holds indices in decreasing order of value.
        monotone_queue = deque()
        left = right = 0
        while right < len(nums):
            # Remove indices whose values are smaller than current.
            while monotone_queue and nums[monotone_queue[-1]] < nums[right]:
                monotone_queue.pop()
            monotone_queue.append(right)

            # Evict the left index if it slid out of the window.
            if left > monotone_queue[0]:
                monotone_queue.popleft()

            if (right + 1) >= k:
                output.append(nums[monotone_queue[0]])
                left += 1
            right += 1

        return output
