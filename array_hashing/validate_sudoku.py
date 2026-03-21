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

from typing import List


class Solution:
    def isValidSudoku(
        self, board: List[List[str]]
    ) -> bool:
        # Plain dicts; setdefault initialises a
        # missing key with an empty set on first use.
        row: dict = {}
        col: dict = {}
        square: dict = {}

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                val = board[r][c]
                sq_key = (r // 3, c // 3)

                # Reject if digit already appears.
                if (
                    val in row.setdefault(r, set())
                    or val in col.setdefault(c, set())
                    or val in square.setdefault(
                        sq_key, set()
                    )
                ):
                    return False

                row[r].add(val)
                col[c].add(val)
                square[sq_key].add(val)

        return True


if __name__ == "__main__":
    sol = Solution()

    # Valid board — expected: True
    valid_board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"],
    ]
    print(sol.isValidSudoku(valid_board))

    # Invalid board (duplicate 8 in first row)
    # — expected: False
    invalid_board = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"],
    ]
    print(sol.isValidSudoku(invalid_board))
