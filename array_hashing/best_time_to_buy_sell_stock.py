"""
You are given an array prices where prices[i] is
the price of a stock on the ith day. Maximize
profit by choosing one day to buy and a future day
to sell. Return 0 if no profit is achievable.

Example:
  Input:  prices=[7,1,5,3,6,4]
  Output: 5

Example:
  Input:  prices=[7,6,4,3,1]
  Output: 0
"""


def maxProfit(prices: list[int]) -> int:
    # Track the cheapest buy price seen so far.
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        # Update the minimum buy price when lower found.
        if price < min_price:
            min_price = price
        # Greedily update profit if this sell beats the best.
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit
