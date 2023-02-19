#problem understanding
    #Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    #An input string is valid if:
        #Open brackets must be closed by the same type of brackets.
        #Open brackets must be closed in the correct order.
        #Every close bracket has a corresponding open bracket of the same type.
#strategy to solve the problem
    #idea if too loop through each element of string for each closed bracket we will have the top open bracket equal to the current closed bracket.
    #using stack to keep track of open bracket
    #using map to map between closed with open 
    #condition to return False:
        #stack is empty. then it open by closed.
        #or the current closed do not match the top open
    #condition to return True
        #loop through all character of string and we have empty stack. Because every open have closed
        #check for the case of empty input string
    #check for precondition
        # if length of string < 2 it can not form a valid parenthesis
    #variable:
        #map (dict): to map between close and open parenthesis
        #stack (list): to keep track of open parentheses
    #why using stack
        #the idea is using stack to keep track of opening bracket. when finding the closed bracket pop it. and check until we do not have anything left
        #using map (or dict) to map between open and close bracket.
        #condition to return False
            #stack is empty or we have a closed bracket but the do not have top of stack equal. 
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