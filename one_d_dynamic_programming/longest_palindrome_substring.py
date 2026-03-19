"""
Given a string s, return the longest palindromic
substring.

Example:
  Input:  s="babad"
  Output: "bab" or "aba"

Constraints:
  Expand around each center to find all palindromes in O(n^2).
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome = ''
        for i in range(len(s)):
            # Check odd-length palindromes centered at i.
            odd = self.get_palindrome(s, i, i)
            # Check even-length palindromes centered between i and i+1.
            even = self.get_palindrome(s, i, i + 1)
            palindrome = max([palindrome, odd, even], key=len)
        return palindrome

    def get_palindrome(self, s: str, left: int, right: int) -> str:
        # Expand outward while characters match.
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
