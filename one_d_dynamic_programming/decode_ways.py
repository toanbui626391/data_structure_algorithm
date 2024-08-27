"""
strategy to solve the problem
    problem: 
        given a string of int s. compute number of way to decode this int string to normal string
    why:
        using dynamic programming for number of combination problem
        for reach index, you have two choice decode the current index or the last two current index
        dp[i] is number of decode way of string with length i
        we need a dp of length len(s) + 1 because dp is a function of len of s and we take substring operation 

"""
"""
Recursive and Memorization style
    Problem: count number of decode way -> count number of leaf which reach to the end of the string
    You need to draw decision tree which we traverse the string
        For each node i there are one or two way to decode it: dfs(i) = dfs(i+1) + dfs(i+2)

"""



class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def dfs(sub_string):
            if not sub_string:
                return 1
            first_case, second_case = 0, 0
            if 1 <= int(sub_string[:1]) <= 9:
                first_case = dfs(sub_string[1:])
            if 10 <= int(sub_string[:2]) <= 26:
                second_case = dfs(sub_string[2:])
            return first_case + second_case
        return dfs(s)