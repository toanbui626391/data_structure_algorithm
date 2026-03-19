"""
Given an m x n matrix where rows are sorted left to
right and each row's first value exceeds the last
row's last value, search for target.

Example:
  Input:  matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]],
          target=3
  Output: True

Constraints:
  Two-pass binary search: find row first, then column.
"""

from typing import List


class Solution:
    def searchMatrix(
        self, matrix: List[List[int]], target: int
    ) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        # Binary search to identify the candidate row.
        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        # No valid row was found.
        if not top <= bot:
            return False

        # Binary search within the identified row.
        left, right = 0, COLS - 1
        while left <= right:
            mid = (left + right) // 2
            if target == matrix[row][mid]:
                return True
            elif target > matrix[row][mid]:
                left = mid + 1
            else:
                right = mid - 1
        return False
