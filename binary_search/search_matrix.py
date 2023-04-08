#problem understanding

#strategy to solve the problem
    #why: 
        #using adoptation binary search. it is a sorted matrix
        #find the row. then check do we need to continue with row search
        #binary search in row
    #varialbes:
        #COLS, ROWS (int): to keep the lenght of row and col
        #top, bot (int): to search for row
        #l, r (int): to search for elemen in row
    #erro notes:
        # ROW, COL = len(matrix) - 1, len(matrix[0]) - 1. remember index = len -1
        # in find row use simmple logic. if elif else


#strategy to solve the problem v2
    #goal: check if target in matrix
    #why:
        #because matrix is in sorted order, we can use binary search
        #the key is to find i (index of row) and j(index of col). find j first and then i
        

############################################reference solution
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False
    
#############################refernce solution 2
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top+bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        
        if not top <= bot: #search all but can not file possible row
            return False

        l, r = 0, COLS -1
        while l <= r:
            middle = (l+r)//2
            if target == matrix[row][middle] :
                return True
            elif target > matrix[row][middle] :
                l = middle + 1
            else:
                r = middle - 1
        return False