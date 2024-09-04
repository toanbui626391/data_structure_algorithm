
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix), len(matrix[0])
        left, right, top, bottom = 0, n - 1, 0, m - 1
        res = []
        while left <= right and top <= bottom:
            #  top left to top right
            for col in range(left,right+1):
                res.append(matrix[top][col])
            top += 1
            # top right to right bottom
            for row in range(top, bottom+1):
                res.append(matrix[row][right])
            right -= 1
            # right bottom to left bottom
            for col in range(right, left-1, -1):
                res.append(matrix[bottom][col])
            bottom -= 1
             # left bottom to left top
            for row in range(bottom, top-1, -1):
                res.append(matrix[row][left])
            left += 1
        # just ignore the redundant and return length of m*n
        return res[:m*n]