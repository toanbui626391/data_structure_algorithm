"""
Problem: Minimum Window Substring

Given strings s and t, return the minimum window
substring of s that contains every character in t
(including duplicates). Return "" if none exists.

Example:
  Input:  s="ADOBECODEBANC", t="ABC"
  Output: "BANC"

Approach: Variable-size sliding window
  - need: dict tracking required chars from t.
  - have: dict tracking chars in current window.
  - count_need: distinct chars in t.
  - count_have: distinct chars meeting required freq.
  - Expand window by moving right pointer.
  - Shrink window from left to minimize length
    while count_have == count_need.
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        # Build requirement map
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        have = {}
        count_need = len(need)
        count_have = 0

        # Track the best (minimum) window
        res_left, res_right = -1, -1
        min_len = float("inf")

        left = 0
        for right in range(len(s)):
            # 1. Expand window
            c = s[right]
            have[c] = have.get(c, 0) + 1

            if c in need and have[c] == need[c]:
                count_have += 1

            # 2. Shrink window while valid
            while count_have == count_need:
                window_len = right - left + 1
                
                # Update minimum window result
                if window_len < min_len:
                    min_len = window_len
                    res_left = left
                    res_right = right

                # Pop left character
                left_c = s[left]
                have[left_c] -= 1

                if left_c in need and have[left_c] < need[left_c]:
                    count_have -= 1

                left += 1

        if min_len != float("inf"):
            return s[res_left : res_right + 1]
        return ""


if __name__ == "__main__":
    sol = Solution()
    print(sol.minWindow("ADOBECODEBANC", "ABC"))
    print(sol.minWindow("a", "a"))
    print(sol.minWindow("a", "aa"))
