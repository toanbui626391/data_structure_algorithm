#problem understanding
    #Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    #An input string is valid if:
        #Open brackets must be closed by the same type of brackets.
        #Open brackets must be closed in the correct order.
        #Every close bracket has a corresponding open bracket of the same type.
#strategy to solve the problem
    #the character in stack have to be open parentheses
    #stack to keep track of non-close parenthesis have to be empty
    # not stack to check of empyt input string
    # check the current close parentheses with the last open parentheses
    #why do we need to use stack in this case:
        #stack will help use to keep track of the most recent open parentheses. Because we have to compare the current close parentheses with the current open parentheses
    #variable:
        #map (dict): to map between close and open parenthesis
        #stack (list): to keep track of open parentheses
###################################reference solution
class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack