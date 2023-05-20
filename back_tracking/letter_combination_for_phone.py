"""
strategy to solve the problem
    problem: 
        given a string of int, find all combination of letter
        combination will have the same lengh of list. Example, [1, 2] and 
    why 
        backtrack(i, curStr) or dfs
            i (int): index of elment in digits
            curStr (str): will add char along the depth of the tree
            add curStr to have more readability and eaiser to logic inside the dfs function
        build maping between digit string with and char string
        each layer is possible elemnt from the i index of digit
        res (list): collect curStr when base case

"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        #build map between int string and char string
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, curStr):
            #base case
            if i == len(digits):
                res.append(curStr)
                return
            for c in digitToChar[digits[i]]: #all possible child
                backtrack(i + 1, curStr + c) #next layer is nex string

        if digits:
            backtrack(0, "")

        return res
