"""
Problem: Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is
the price of a stock on the ith day. Find the
maximum profit you can achieve from one transaction.

Example:
  Input:  prices = [7,1,5,3,6,4]
  Output: 5  (Buy at 1, sell at 6)

Approach: Two Pointers / Sliding Window
  - Left pointer `buy` tracks the lowest price.
  - Right pointer `sell` scans sequentially.
  - If we find a lower price, move `buy` to `sell`.
  - Otherwise, calculate profit and update max.
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Left pointer (buy day), right pointer (sell day)
        buy = 0
        max_profit = 0
        
        for sell in range(1, len(prices)):
            # If current price is lower than our buy price,
            # this is our new optimal buy point.
            if prices[sell] < prices[buy]:
                buy = sell
            else:
                # Calculate profit if we sold today
                profit = prices[sell] - prices[buy]
                max_profit = max(max_profit, profit)
                
        return max_profit
