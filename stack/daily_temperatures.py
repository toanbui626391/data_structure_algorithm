"""

strategy to solve the problem:
    #daily temperature problem: find the number of day from the ith day will have warmer temperature

    #using stack strategy:
        res (list): to hold result list
        stack (list): to hold the index, temperature of daly
        #for each iteration we will know the index (date) and it's temperature
            #if 
"""
 
#############################################reference solution
from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: #find result of all date in stack
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i)) #build stack
        return res