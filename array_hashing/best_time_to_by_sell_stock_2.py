"""
You may complete as many transactions as you like.
Add profit for every day the price rises, which
captures every upswing without missing any.

Example:
  Input:  prices=[7,1,5,3,6,4]
  Output: 7
"""


def maxProfit(prices: list[int]) -> int:
    total_profit = 0

    # Accumulate profit for each up-day individually.
    for i in range(1, len(prices)):
        # Each positive gap represents a profitable transaction.
        if prices[i] > prices[i - 1]:
            total_profit += prices[i] - prices[i - 1]

    return total_profit
