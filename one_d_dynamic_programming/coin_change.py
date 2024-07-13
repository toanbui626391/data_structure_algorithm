"""
strategy to solve the problem
    problem:
        given a list of coins and amount (int). compute mininum of coins to make up that amount. return -1 if we can not make change
    why:
        using dynamic programming for choosing element from list
        dp[a] is number of coins need to make up for amount a
        dp[a] = min(dp[a], dp[a-c])
        dp[a-c] = is number of coins need to make up for amount a when we choose c in result set  
        dp of length amount + 1 because dp[a] is not index but integer value


"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [float("inf")] * (amount+1)
        dp[0] = 0 #if amount is zero then we need no coins
        for c in coins:
            for j in range(c, amount+1):
                dp[j] = min(dp[j], dp[j-c] + 1)
        return -1 if dp[-1] == float("inf") else dp[-1] #if coins have not make up the amount then return -1 else return dp[-1]