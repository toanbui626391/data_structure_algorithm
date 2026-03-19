"""
Determine if a 9x9 Sudoku board is valid. Only
filled cells need to be validated:
  - Each row must contain digits 1-9 without repeat.
  - Each column must contain digits 1-9 without repeat.
  - Each 3x3 sub-box must contain 1-9 without repeat.

Example:
  Input:  valid 9x9 board
  Output: True or False
"""

from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(
        self, board: List[List[str]]
    ) -> bool:
        # Sets indexed by row, col, or sub-square key.
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                # Reject if the digit already appears.
                if (
                    board[r][c] in row[r]
                    or board[r][c] in col[c]
                    or board[r][c] in square[(r // 3, c // 3)]
                ):
                    return False
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                square[(r // 3, c // 3)].add(board[r][c])
        return True
