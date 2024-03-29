"""
strategy to solve the problem
    problem:
        given a matrix size m*n of "X" and "O". Flip the surrounded (four directions) area of "O" to "X".
    why:
        if outer ring of matrix is "0" then it is not surrounded. we start from the outer ring to flip "0" to "T"
        flip every "0" left to "X" because it cell is surrouned
        flip back "T" to "O" 
"""
from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def capture(r, c):
            """
            convert cell "O" to "T"
            """
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O":
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # 1. (DFS) Capture unsurrounded regions (O -> T)
        for r in range(ROWS):
            for c in range(COLS):
                #starting point for search is from outter cell because we know it will not be surrounded if it is "O"
                #condition for outer cel (r in [0, h-1] or c in [0, w-1])
                if board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1]):
                    capture(r, c)

        # 2. Capture surrounded regions (O -> X)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # 3. Uncapture unsurrounded regions (T -> O)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
