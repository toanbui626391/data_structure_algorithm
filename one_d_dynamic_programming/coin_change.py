"""
Problem:
Given a list of coin denominations and an amount,
return the minimum number of coins needed to make
up the amount. Return -1 if impossible.

Examples:
Input: coins = [1, 5, 11], amount = 15
Output: 3

Constraints:
1 <= coins.length <= 12
1 <= coins[i] <= 2^31 - 1
0 <= amount <= 10^4
"""

from typing import List


class Solution:
    def coinChange(
        self, coins: List[int], amount: int
    ) -> int:
        # Initialize the dp array with infinity.
        # We use amount + 1 as a safe "infinity" because
        # the max possible coins needed would be 'amount'.
        dp = [amount + 1] * (amount + 1)
        
        # Base case: 0 coins needed to make amount 0.
        dp[0] = 0
        
        # Iterate through each coin first (Combination).
        for c in coins:
            # For each coin, update all reachable amounts.
            # Start at 'c' since we can't make smaller amounts.
            for a in range(c, amount + 1):
                # The core DP formula.
                dp[a] = min(dp[a], dp[a - c] + 1)
                    
        # If the target amount is still "infinity", return -1.
        if dp[amount] == amount + 1:
            return -1
            
        return dp[amount]


if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1
    coins1 = [1, 5, 11]
    amount1 = 15
    res1 = sol.coinChange(coins1, amount1)
    
    print("Test 1:")
    print(f"Input: coins={coins1}, amount={amount1}")
    print(f"Output: {res1}")
    print()
    
    # Test case 2
    coins2 = [2]
    amount2 = 3
    res2 = sol.coinChange(coins2, amount2)
    
    print("Test 2:")
    print(f"Input: coins={coins2}, amount={amount2}")
    print(f"Output: {res2}")
