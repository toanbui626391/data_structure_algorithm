"""
Problem: Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is
the price of a stock on the ith day. Maximize
profit by choosing one day to buy and a future day
to sell. Return 0 if no profit is achievable.

Example:
  Input:  prices=[7,1,5,3,6,4]
  Output: 5  (Buy at 1, sell at 6)

Approach: Greedy / One Pass
  - Track the cheapest buy price seen so far.
  - For each day, check if selling today yields
    a better profit than our current max_profit.
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            # Update the minimum buy price history
            if price < min_price:
                min_price = price
                
            # Greedily update profit
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit
