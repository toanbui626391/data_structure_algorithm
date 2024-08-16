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
        dp = {}
        return self._dp_helper(s, dp)

    def _dp_helper(self, data, dp):
        # Base Case 1: Empty string
        if not data:
            return 1
        first_call, second_call = 0, 0
        if data in dp:
            return dp[data]
        if 1 <= int(data[:1]) <= 9:
            first_call = self._dp_helper(data[1:], dp)
        if 10 <= int(data[:2]) <= 26:
            second_call = self._dp_helper(data[2:], dp)
        dp[data] = first_call + second_call
        return dp[data]