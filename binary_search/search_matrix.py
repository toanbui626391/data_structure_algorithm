"""
Problem: Search a 2D Matrix

Given an m x n matrix where rows are sorted left to
right and each row's first value exceeds the last
row's last value, search for target.

Example:
  Input:  matrix=[[1,3,5,7],[10,11,16,20]], target=3
  Output: True

Approach: Two-Pass Binary Search
  - Pass 1: Binary search the first column of each
    row to find the candidate row.
  - Pass 2: Binary search that specific row.
"""

from typing import List


class Solution:
    def searchMatrix(
        self, matrix: List[List[int]], target: int
    ) -> bool:
        
        rows, cols = len(matrix), len(matrix[0])

        # 1. Binary search to find candidate row
        top = 0
        bot = rows - 1
        row_cand = -1

        while top <= bot:
            mid_row = top + (bot - top) // 2
            
            if target > matrix[mid_row][-1]:
                top = mid_row + 1
            elif target < matrix[mid_row][0]:
                bot = mid_row - 1
            else:
                row_cand = mid_row
                break

        if row_cand == -1:
            return False

        # 2. Binary search within that specific row
        left = 0
        right = cols - 1
        row = matrix[row_cand]

        while left <= right:
            mid = left + (right - left) // 2
            
            if row[mid] == target:
                return True
            elif row[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
                
        return False
