class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @cache
        def dfs(i, target):
            if target == amount:
                return 1
            if target > amount:
                return 0
            if i >= len(coins):
                return 0
            #to make combination, each node have two child node, 1. take i, 2 not take i
            #dfs(i, total+coins[i]) -> take i and continue with all current option
            #dfs(i+1, total) -> not take i and reduce element to choose from
            return dfs(i, target+coins[i]) + dfs(i+1, target)
        return dfs(0, 0)


        