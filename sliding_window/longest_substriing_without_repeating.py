"""
Problem: Longest Substring Without Repeating Chars

Given a string s, find the length of the longest
substring without repeating characters.

Example:
  Input:  s="abcabcbb"
  Output: 3  ("abc")

Approach: Sliding Window
  - Use a HashSet to track unique characters in
    the current window.
  - Expand the right pointer.
  - If a duplicate is found, shrink the left
    pointer until the duplicate is removed.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        window_chars = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            # If we see a duplicate, shrink from left
            # until the duplicate is removed from the set.
            while s[right] in window_chars:
                window_chars.remove(s[left])
                left += 1
                
            # Now it's safe to add the right character
            window_chars.add(s[right])
            
            # Update our maximum length found
            current_len = right - left + 1
            max_len = max(max_len, current_len)
            
        return max_len
