"""
strategy to solve the problem
    problem:
        given string s and a list of words wordDict. check can we break s in to space separated or not
    why:
        using dynamic programming for a subarray problem
        loop from 1 to len(s+1) because the edge case of s[j:i] when i is the last element of
        dp[i] is the right index of substring
        condition to be a word is the left index is the right index of other word and that word in wordDict
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s)

        for i in range(1, len(s)+1):
            for j in range(i+1):
                if dp[j] and s[j:i] in wordDict: #the left index is mark at starting of a word
                    dp[i] = True #the righ index is also the left index of other words
        return dp[-1]