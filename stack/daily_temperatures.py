#problem understanding
#Given an array of integers temperatures represents the daily temperatures,
#return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
#If there is no future day for which this is possible, keep answer[i] == 0 instead.

#strategy to solve the proble
    #using stack to keep track of daily temperature which is smaller or decrese
    #when stack is not empty and t > the first position (largest one) compute number of date we have higher temperature.
        #calculate number of date for given index
    #variable
        #res (list): to store 
        #stack (decrease daily temperatures): to store decrease
    #why using stack
        #for each return position we have to check the current temmperature with the follow temperature until you can meet higher temperature
        #keep decrease value stack allow just to check when we higher temperature
        #stack also allow us to caculate index different for all lower temp by poping those value   
#############################################reference solution
from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res