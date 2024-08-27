class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memory = {}  # Memoization dictionary to store computed results
        
        def dfs(i, j):
            # Check if the result for the current indices is already memoized
            if (i, j) in memory:
                return memory[(i, j)]
            
            # Base cases
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False

            # Check if the current characters match or if the pattern character is '.'
            same = i < len(s) and (s[i] == p[j] or p[j] == ".")
            
            # If the next character in pattern is '*', handle the '*' wildcard character
            if (j + 1) < len(p) and p[j + 1] == "*":
                # Explore both options: matching zero occurrences and matching current character
                memory[(i, j)] = dfs(i, j + 2) or (same and dfs(i + 1, j))
                return memory[(i, j)]
            
            # If the characters match, move to the next characters in both strings
            if same:
                memory[(i, j)] = dfs(i + 1, j + 1)
                return memory[(i, j)]
            
            # If none of the above cases match, return False
            memory[(i, j)] = False
            return False

        # Start the DFS from the beginning of both strings
        return dfs(0, 0)