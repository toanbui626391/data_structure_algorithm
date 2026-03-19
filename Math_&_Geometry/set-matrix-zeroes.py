"""
Given an m x n matrix, if any element is 0,
set its entire row and column to 0 in place.

Example:
  Input:  matrix=[[1,1,1],[1,0,1],[1,1,1]]
  Output: [[1,0,1],[0,0,0],[1,0,1]]

Constraints:
  First collect all zero positions; then apply
  zeros to those rows and columns separately.
"""

from typing import List


class Solution:
    def setZeroes(
        self, matrix: List[List[int]]
    ) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        zero_rows: set = set()
        zero_cols: set = set()

        # Record which rows and columns contain zero.
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        # Zero out the recorded rows.
        for row in zero_rows:
            for j in range(cols):
                matrix[row][j] = 0

        # Zero out the recorded columns.
        for col in zero_cols:
            for i in range(rows):
                matrix[i][col] = 0
