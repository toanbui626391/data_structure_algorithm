# problem understanding
#     Given n pairs of parentheses, write a function to generate all
#     combinations of well-formed parentheses.
#
# strategy to solve the problem
#     using stack to build a stack of valid open and close parentheses
#     variable
#         stack
#         res
#         openN
#         closeN
# strategy to solve the problem v2:
#     this is binary tree problem and not a stack problem
#     we can use depth first search and crecursive call to sole this problem
#     have to form valid parentheses string. Therefore number of open have to >=
#     number of close
#     limit n pair of parentheses. Therefore number of open <= n
#
#     variables:
#         num_open (int): number of open parentheses
#         num_close (int): number of close parentheses
#         string (string): current string of the current node
###########################################################reference solution
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res
    

##############################################reference solution v2
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(num_open, num_close, string):
            if num_open == num_close == n:
                res.append(string)
                return
            if num_open < n:
                dfs(num_open + 1, num_close, string + "(")
            if num_open > num_close:
                dfs(num_open, num_close + 1, string + ")")
        res = []
        dfs(0, 0, "")
        return res
