class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])  # Get the number of rows and columns in the matrix
        memory = {}  # Initialize a memoization dictionary

        def dfs(r, c, prevVal):
            # Base cases: Check if out of bounds or current cell value is not increasing
            if r < 0 or r == ROWS or c < 0 or c == COLS or matrix[r][c] <= prevVal:
                return 0
            # Memoization check: If result for current cell already computed, return it
            if (r, c) in memory:
                return memory[(r, c)]

            ans = 1  # Initialize the answer to 1 (minimum length of increasing path)
            # Explore all four directions from the current cell
            ans = max(ans, 1 + dfs(r + 1, c, matrix[r][c]))  # Down
            ans = max(ans, 1 + dfs(r - 1, c, matrix[r][c]))  # Up
            ans = max(ans, 1 + dfs(r, c + 1, matrix[r][c]))  # Right
            ans = max(ans, 1 + dfs(r, c - 1, matrix[r][c]))  # Left
            memory[(r, c)] = ans  # Memoize the result for the current cell
            return ans  # Return the length of the longest increasing path starting from the current cell

        # Iterate through each cell in the matrix and call the DFS function
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)  # Start DFS from each cell with initial previous value -1
        return max(memory.values())  # Return the maximum value stored in the memoization dictionary