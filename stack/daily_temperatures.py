"""
Problem: Daily Temperatures

Given an array of temperatures, return an array
where each entry is the number of days until a
warmer temperature. If no warmer day exists,
use 0.

Example:
  Input:  temperatures = [73,74,75,71,69,72,76,73]
  Output: [1,1,4,2,1,1,0,0]

Approach: Monotonically Decreasing Stack
  - Use a stack to store indices of days we
    haven't found a warmer temperature for yet.
  - When we find a warmer day, pop the colder
    days from the stack and calculate the
    difference in indices.
"""

from typing import List


class Solution:
    def dailyTemperatures(
        self, temperatures: List[int]
    ) -> List[int]:
        
        n = len(temperatures)
        res = [0] * n
        # Stack stores indices of temperatures
        stack = []

        for i, temp in enumerate(temperatures):
            # While today is warmer than the day at
            # the top of the stack, resolve it!
            while stack and temp > temperatures[stack[-1]]:
                colder_day_index = stack.pop()
                res[colder_day_index] = i - colder_day_index
            
            # Add today's index to be resolved later
            stack.append(i)

        return res
