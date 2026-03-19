"""
Given an array of temperatures, return an array
where each entry is the number of days until a
warmer temperature. If no warmer day exists, use 0.

Example:
  Input:  temperatures=[73,74,75,71,69,72,76,73]
  Output: [1,1,4,2,1,1,0,0]

Constraints:
  A monotonic stack resolves each temperature in O(n) total.
"""

from typing import List


class Solution:
    def dailyTemperatures(
        self, temperatures: List[int]
    ) -> List[int]:
        result = [0] * len(temperatures)
        # Stack holds (temperature, index) pairs.
        stack = []

        for i, temp in enumerate(temperatures):
            # Pop all stack entries colder than today.
            while stack and temp > stack[-1][0]:
                stack_temp, stack_index = stack.pop()
                result[stack_index] = i - stack_index
            stack.append((temp, i))
        return result
