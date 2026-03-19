"""
Given an m x n matrix of 'X' and 'O', capture all
regions surrounded by 'X'. A region is captured by
flipping all 'O's into 'X's. 'O' on or connected
to the border cannot be captured.

Example:
  Input:  board=[["X","X","X","X"],["X","O","O","X"],
          ["X","X","O","X"],["X","O","X","X"]]
  Output: [["X","X","X","X"],["X","X","X","X"],
          ["X","X","X","X"],["X","O","X","X"]]

Constraints:
  Mark border-connected 'O' cells as temporary 'T', then flip.
"""

from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        def capture(r, c):
            """
            DFS to mark border-connected 'O' cells as 'T'.
            """
            if (
                r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or board[r][c] != "O"
            ):
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # Mark all 'O' cells reachable from the border.
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (
                    r in [0, ROWS - 1] or c in [0, COLS - 1]
                ):
                    capture(r, c)

        # Flip remaining 'O' (surrounded) to 'X'.
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # Restore border-connected cells back to 'O'.
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
