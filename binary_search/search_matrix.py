#problem understanding

#strategy to solve the problem
    #why: 
        #each row is sorted, follow row value always larger than previuos row.
        #=> use binary search for row and then each value in row
        # if not to <= bot then there is no possible row to search for result
        #note: should use target as a reference point for for binary search reasoning
    #varialbes:
        #COLS, ROWS (int): to keep the lenght of row and col
        #top, bot (int): to search for row
        #l, r (int): to search for elemen in row


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