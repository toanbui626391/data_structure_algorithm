"""
Place n queens on an n x n chessboard such that
no two queens attack each other. Return all
distinct valid board configurations.

Example:
  Input:  n=4
  Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

Constraints:
  Track column, positive diagonal, and negative diagonal sets.
"""

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        # (r+c) identifies positive diagonals.
        pos_diag = set()
        # (r-c) identifies negative diagonals.
        neg_diag = set()

        result = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            # A complete board configuration is found.
            if r == n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return

            for c in range(n):
                # Skip positions under attack.
                if (
                    c in col
                    or (r + c) in pos_diag
                    or (r - c) in neg_diag
                ):
                    continue

                # Place a queen and update attack sets.
                col.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                # Remove the queen to try the next column.
                col.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return result
