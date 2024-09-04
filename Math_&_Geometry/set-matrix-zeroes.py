class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        zero_rows, zero_cols = set(), set()

        # First pass: record the rows and columns that are to be zeroed
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        # Second pass: set the rows to zero
        for row in zero_rows:
            for j in range(cols):
                matrix[row][j] = 0

        # Third pass: set the columns to zero
        for col in zero_cols:
            for i in range(rows):
                matrix[i][col] = 0