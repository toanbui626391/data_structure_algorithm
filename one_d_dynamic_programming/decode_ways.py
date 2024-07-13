"""
strategy to solve the problem
    problem: 
        given a string of int s. compute number of way to decode this int string to normal string
    why:
        using dynamic programming for number of combination problem
        for reach index, you have two choice decode the current index or the last two current index
        dp[i] is number of decode way of string with length i
        we need a dp of length len(s) + 1 because dp is a function of len of s and we take substring operation 

"""
class Solution:
    def numDecodings(self, s: str) -> int:
        #check for invalid case
        if s[0] == "0":
            return 0

        dp = [0] * (len(s)+1)
        dp[0], dp[1] = 1, 1
        for i in range(2, len(s)+1):
            if 1 <= int(s[i-1:i]) <= 9:
                dp[i] += dp[i-1]
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        return dp[-1]