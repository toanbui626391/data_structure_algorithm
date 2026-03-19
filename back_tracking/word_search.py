"""
Given an m x n grid of characters and a word,
return true if the word exists in the grid.
The word must be formed by adjacent cells; the
same cell may not be used more than once.

Example:
  Input:  board=[["A","B","C","E"],["S","F","C","S"],
          ["A","D","E","E"]], word="ABCCED"
  Output: True

Constraints:
  Mark cells visited during DFS; restore after backtracking.
"""

from typing import List


class Solution:
    def exist(
        self, board: List[List[str]], word: str
    ) -> bool:
        if not board:
            return False

        num_rows = len(board)
        num_cols = len(board[0])

        def dfs_search(idx: int, row: int, col: int) -> bool:
            """
            Return True if word[idx:] can be matched starting
            at board[row][col].
            """
            if (
                col < 0
                or col == num_cols
                or row < 0
                or row == num_rows
                or word[idx] != board[row][col]
            ):
                return False
            if idx == len(word) - 1:
                return True
            saved = board[row][col]
            # Temporarily mark cell to prevent reuse.
            board[row][col] = '#'
            found = (
                dfs_search(idx + 1, row, col + 1)
                or dfs_search(idx + 1, row, col - 1)
                or dfs_search(idx + 1, row + 1, col)
                or dfs_search(idx + 1, row - 1, col)
            )
            board[row][col] = saved
            return found

        return any(
            dfs_search(0, row, col)
            for row in range(num_rows)
            for col in range(num_cols)
        )
