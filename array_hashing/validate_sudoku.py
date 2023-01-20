#problem understand
    #Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
        #Each row must contain the digits 1-9 without repetition.
        #Each column must contain the digits 1-9 without repetition.
        #Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

    #check duplicate for a collection -> using hash set

#solution strategy:
    # row (defaultdict(set)): to collect elements in each row
    # col (defaultdict(set)): to collect elements in each col
    # sqaure (defaultdict(set)): to collect elements in sub square
    # how to index collection for row, col and sub sqare
        #for col and row use col and row index of matrix
        #for index of sub squre use key (r//3, c//3)
    # integer operators is: //
#######################################solution reference
from collections import defaultdict
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)
        for r in range(3):
            for c in range(3):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in row[r] or
                    board[r][c] in col[c] or
                    board[r][c] in square[(r//3, c//3)]
                ):
                    return False
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                square[(r//3, c//3)].add(board[r][c])
        return True
