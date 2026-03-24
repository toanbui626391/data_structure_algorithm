"""
Problem: Best Time to Buy and Sell Stock II

You may complete as many transactions as you like.
Find the maximum profit.

Example:
  Input:  prices=[7,1,5,3,6,4]
  Output: 7

Approach: Greedy
  - Add profit for every day the price rises.
  - This captures every upswing without missing 
    any profitable micro-transactions.
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0

        # Accumulate profit for each up-day separately.
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                total_profit += prices[i] - prices[i - 1]

        return total_profit
