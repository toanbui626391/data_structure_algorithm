"""
N-Queens backtracking reference implementation.
Place n non-attacking queens on an n x n board.

Example:
  Input:  n=4
  Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
"""

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        pos_diag = set()
        neg_diag = set()

        result = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return

            for c in range(n):
                # Skip if any attack set includes this position.
                if (
                    c in col
                    or (r + c) in pos_diag
                    or (r - c) in neg_diag
                ):
                    continue

                col.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                # Undo placement for the next candidate.
                col.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return result
