"""
strategy to solve the problem
    problem:
        given n queens in n*n chess board. Find all queen position which they do not attach each others
    why:
        backtracing(r) or dfs
            r (int): row index
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
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
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