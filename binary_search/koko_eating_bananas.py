"""
Problem: Koko Eating Bananas

Koko loves to eat bananas. There are n piles of
bananas, the ith pile has piles[i] bananas. The
guards have gone and will come back in h hours.

Find the minimum bananas-per-hour eating speed (k)
that allows Koko to eat all bananas before the
guards return.

Example:
  Input:  piles=[3,6,7,11], h=8
  Output: 4

Approach: Binary Search on Answer
  - The minimum speed is 1, max is max(piles).
  - Use binary search to find the minimum valid
    speed `k` that satisfies total_time <= h.
"""

from typing import List
import math


class Solution:
    def minEatingSpeed(
        self, piles: List[int], h: int
    ) -> int:
        
        # Binary search space for speed k
        left = 1
        right = max(piles)
        
        best_speed = right

        while left <= right:
            mid_speed = left + (right - left) // 2
            
            # Calculate total time at this speed
            total_time = 0
            for p in piles:
                total_time += math.ceil(p / mid_speed)

            if total_time <= h:
                # This speed works! Try finding a
                # slower (smaller) working speed.
                best_speed = min(best_speed, mid_speed)
                right = mid_speed - 1
            else:
                # Too slow, need to eat faster
                left = mid_speed + 1
                
        return best_speed
