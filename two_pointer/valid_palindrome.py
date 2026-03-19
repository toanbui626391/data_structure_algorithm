"""
A phrase is a palindrome if, after converting to
lowercase and removing non-alphanumeric characters,
it reads the same forward and backward.

Example:
  Input:  s="A man, a plan, a canal: Panama"
  Output: True

Constraints:
  Use two pointers to avoid building a new string.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            # Advance past non-alphanumeric characters.
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            # Case-insensitive comparison from both ends.
            if s[left].lower() != s[right].lower():
                return False
            left, right = left + 1, right - 1
        return True
