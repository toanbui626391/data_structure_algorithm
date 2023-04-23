"""
strategy to solve the problem
    problem
        given a board m*n of char, check exist workd
        word is contruct by adjacent char, same char cell may not be used more than one
    why
        dfs(i, x, y):
            i (int): index of element in word
            x, y (int): index of col and row in board
        base case for False: out of bound for x and y or word[i] != board[y][x]
        condition to stop search and return True: i == len(word) - 1. because at i we have alread check and then return
        search at each step: 
            dfs(i+1, x+1, y) #
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        if not board: 
            # Quick response for empty board
            return False
        
        h, w = len(board), len(board[0])
      
        def dfs_search(idx: int, x: int, y: int) -> bool:
            """
            check the current letter in word equal to current letter in board
            """
            
            if x < 0 or x == w or y < 0 or y == h or word[idx] != board[y][x]:
                # Reject if out of boundary, or current grid cannot match the character word[idx]
                return False
            if idx == len(word) - 1: 
                # Accept when we match all characters of word during DFS
                return True
            cur = board[y][x]      
            # mark as '#' to avoid repeated traversal
            board[y][x] = '#'            
            # visit next four neighbor grids
            found = (
                dfs_search(idx + 1, x + 1, y) or #right
                dfs_search(idx + 1, x - 1, y) or #left
                dfs_search(idx + 1, x, y + 1) or  #below
                dfs_search(idx + 1, x, y - 1)) #adobe
            # recover original grid character after DFS is completed
            board[y][x] = cur
            return found
        # ------------------------------------------------------
        return any(dfs_search(0, x, y) for y in range(h) for x in range(w)) #have to check all possible solution
        