"""
strategy to solve the problem
    problem:
        given n queens in n*n chess board. Find all queen position which they do not attach each others
    why:
        this is problem which we find combination of r, c but queen in board[r][c] can not attact each other.
            board[r][c] can not attact each other so we just skip this position
            we keep track of sets col, posDiag, negDiag because queen can attact horizontal, vertical, positve and negative niagnal
        backtracing(r) or dfs
            r (int): row index
            #base case, when traverse all row (r == n) collect  borad. board is a list of row string
            #condition for invalid board column index have been placed a quen or c in col
            #positive diagnal: (r+c) in positive diagnal set
            #negative diagnal: (r-c) in negative diagnal set

            if valid board, we have to update col, positiveDiagnal, negativeDiagnal and board[c][r]

            dfs(r+1)

            #when use for for all child build back the input col, pos_diag, neg_diag and board
"""

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set()  # (r + c)
        negDiag = set()  # (r - c)

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            #when traversa all layer or row
            if r == n: 
                #append a valid board. a boar is a list of string
                copy = ["".join(row) for row in board] 
                res.append(copy)
                return

            for c in range(n): #all possible col position is child
                #quen can not be the same col. c in col where col is collection of col index which have been place quen
                #quen can not be in the same positive diagnal. r + c
                #quen can not be in the same negative diganl. r - c
                if c in col or (r + c) in posDiag or (r - c) in negDiag: #invalidt board 
                    continue
                
                #update col set, positive diagnal, negative diagnal.
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                #go to next layer
                backtrack(r + 1) #layer is row index

                #reverse back for next child in the same layer
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res