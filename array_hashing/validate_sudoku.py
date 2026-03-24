"""
Problem: Valid Sudoku

Determine if a 9x9 Sudoku board is valid. Only
filled cells need to be validated according to
the standard Sudoku rules.

Example:
  Input:  valid 9x9 board
  Output: True or False

Approach: Hash Sets
  - Use a HashSet for each row, column, and 3x3 
    square to track seen numbers.
  - The 3x3 squares can be indexed by dividing
    the row and column by 3: `(r//3, c//3)`.
"""

import collections
from typing import List


class Solution:
    def isValidSudoku(
        self, board: List[List[str]]
    ) -> bool:
        
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                    
                val = board[r][c]
                square_key = (r // 3, c // 3)
                
                # Check for duplicates using sets
                if (val in rows[r] or 
                    val in cols[c] or 
                    val in squares[square_key]):
                    return False
                    
                # Add to sets to track for future
                cols[c].add(val)
                rows[r].add(val)
                squares[square_key].add(val)
                
        return True
