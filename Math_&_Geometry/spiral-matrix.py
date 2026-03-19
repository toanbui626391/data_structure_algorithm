"""
Given an m x n matrix, return all elements in
spiral order (clockwise from top-left).

Example:
  Input:  matrix=[[1,2,3],[4,5,6],[7,8,9]]
  Output: [1,2,3,6,9,8,7,4,5]

Constraints:
  Shrink four boundaries after traversing each
  side; trim result to m*n to discard overlap.
"""

from typing import List


class Solution:
    def spiralOrder(
        self, matrix: List[List[int]]
    ) -> List[int]:
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        left, right = 0, num_cols - 1
        top, bottom = 0, num_rows - 1
        result = []

        while left <= right and top <= bottom:
            # Traverse top row left to right.
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1

            # Traverse right column top to bottom.
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1

            # Traverse bottom row right to left.
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

            # Traverse left column bottom to top.
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

        # Trim extra elements from corner overlaps.
        return result[:num_rows * num_cols]
