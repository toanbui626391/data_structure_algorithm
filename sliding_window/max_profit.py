"""
Find maximum profit from buying and selling a stock.
Track the lowest price seen so far as the buy point.

Example:
  Input:  prices=[7,1,5,3,6,4]
  Output: 5

Constraints:
  Can only hold one stock at a time; buy before sell.
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        # Sliding window with lowest price as implicit left.
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            result = max(result, price - lowest)
        return result
