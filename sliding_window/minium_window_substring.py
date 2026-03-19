"""
Given strings s and t, return the minimum window
substring of s that contains every character in t
(including duplicates). Return "" if none exists.

Example:
  Input:  s="ADOBECODEBANC", t="ABC"
  Output: "BANC"

Constraints:
  Track "have" vs "need" to know when window is valid.
"""

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        counter_t = Counter(t)
        counter_window = Counter()

        have = 0
        need = len(counter_t)
        result = [-1, -1]
        result_len = float("infinity")
        left = 0
        for r in range(len(s)):
            char = s[r]
            counter_window[char] += 1

            # A character satisfies its required count.
            if (
                char in counter_t
                and counter_window[char] == counter_t[char]
            ):
                have += 1

            while have == need:
                # Update result if this window is smaller.
                if (r - left + 1) < result_len:
                    result = [left, r]
                    result_len = r - left + 1
                # Shrink from the left and update counts.
                counter_window[s[left]] -= 1
                if (
                    s[left] in counter_t
                    and counter_window[s[left]] < counter_t[s[left]]
                ):
                    have -= 1
                left += 1
        left, r = result
        return s[left: r + 1] if result_len != float("infinity") else ""
