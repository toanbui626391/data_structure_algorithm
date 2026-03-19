"""
Rotate an n x n matrix 90 degrees clockwise
in place.

Example:
  Input:  matrix=[[1,2,3],[4,5,6],[7,8,9]]
  Output: [[7,4,1],[8,5,2],[9,6,3]]

Constraints:
  Transpose (swap across diagonal) then reverse
  each row to achieve 90-degree rotation.
"""

from typing import List


class Solution:
    def rotate(
        self, matrix: List[List[int]]
    ) -> None:
        def transpose(mat):
            # Swap elements across the main diagonal.
            for i in range(len(mat)):
                for j in range(i, len(mat[0])):
                    mat[i][j], mat[j][i] = (
                        mat[j][i], mat[i][j]
                    )

        def reverse_rows(mat):
            # Mirror each row around its midpoint.
            for r in range(len(mat)):
                left, right = 0, len(mat) - 1
                while left < right:
                    mat[r][left], mat[r][right] = (
                        mat[r][right], mat[r][left]
                    )
                    left += 1
                    right -= 1

        transpose(matrix)
        reverse_rows(matrix)
