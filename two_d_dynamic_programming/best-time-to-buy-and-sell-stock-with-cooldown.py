class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @cache
        def dfs(i, buying):
            #base case, when finish traverse the tree
            if i >= len(prices):
                return 0
            #compute max profit
            profit_cool = dfs(i+1, buying)
            if buying:
                #if buy then current profit is child profit - buy prices
                #if buy then must sell or cool
                profit_buy = dfs(i+1, not buying) - prices[i]
                return max(profit_cool, profit_buy)
            else:
                #if sell then current profit = child profit + sell prices
                #when sell can only buy after one date of cool
                profit_sell = dfs(i+2, not buying) + prices[i]
                return max(profit_cool, profit_sell)
        #start at index 0 and buying
        return dfs(0, True)