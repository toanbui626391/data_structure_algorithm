"""
Given a string s, find the length of the longest
substring without repeating characters.

Example:
  Input:  s="abcabcbb"
  Output: 3

Constraints:
  Expand right; shrink left until no duplicate exists.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Track characters currently in the window.
        char_set = set()
        left = 0
        result = 0

        for r in range(len(s)):
            # Remove leftmost chars until the duplicate is gone.
            while s[r] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[r])
            result = max(result, r - left + 1)
        return result
