"""
Problem: Valid Palindrome

A phrase is a palindrome if, after converting to
lowercase and removing non-alphanumeric characters,
it reads the same forward and backward.

Example:
  Input:  s="A man, a plan, a canal: Panama"
  Output: True

Approach: Two Pointers (Converging)
  - Left pointer starts at the beginning.
  - Right pointer starts at the end.
  - Skip non-alphanumeric characters.
  - Compare lowercase characters; if they don't
    match, it's not a palindrome.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        
        while left < right:
            # Skip non-alphanumeric characters from left
            while left < right and not s[left].isalnum():
                left += 1
                
            # Skip non-alphanumeric characters from right
            while left < right and not s[right].isalnum():
                right -= 1
                
            # Check characters case-insensitively
            if s[left].lower() != s[right].lower():
                return False
                
            left += 1
            right -= 1
            
        return True
