#strategy to solve the problem
    #goal:  find maximum profit, if can not find profit return 0

    #why:
        #because you can only have profit when you have bougt stock before. Therefore using sliding window technique
        #find lowest bought price in the past is O(n)
        #the key idea:
            #keep track of the lowest prices in the past and compare to the current price to see profit
    
    #variables
        #res (int): to search for result
        #lowest (int): to keep track of the lowest price in the past
###########################################################################reference solution
"""
sliding window technique:
    we use two pointer (left, right) to loop through array of number
    both will start at the begining the the array.
    usually the right will move first and every step
    for each step of right we will decide how to move the left base on some condition

aplly sliding window:
    maxProfix: find max profit for selling stock
    l, r = 0, 0
    for each iteration move right
    keep lowest buying prices. If we have lowest buying prices update it or update left index
    for each iteration compute possible profit to find max profit

"""
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res,price - lowest)
        return res