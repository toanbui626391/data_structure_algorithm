"""
Problem: Longest Repeating Character Replacement

Given a string s and an integer k, return the
length of the longest substring containing the
same letter after performing at most k character
replacements.

Example:
  Input:  s="ABAB", k=2
  Output: 4  (Replace both 'B's with 'A's)

Approach: Sliding Window
  - Track character frequencies in the window.
  - A window is valid if:
    (length of window) - (most frequent char) <= k
  - If the window becomes invalid, shrink it from
    the left until it is valid again.
"""


class Solution:
    def characterReplacement(
        self, s: str, k: int
    ) -> int:
        
        counts = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
            # 1. Expand the window
            char = s[right]
            counts[char] = counts.get(char, 0) + 1

            # Determine the current window size and 
            # the frequency of the most common char.
            window_len = right - left + 1
            max_freq = max(counts.values())

            # 2. Shrink the window if it's invalid
            # Invalid = we need more than k replacements
            while (window_len - max_freq) > k:
                left_char = s[left]
                counts[left_char] -= 1
                left += 1
                
                # Update window metrics after shrinking
                window_len = right - left + 1
                max_freq = max(counts.values())

            # 3. Update the maximum valid window seen
            max_len = max(max_len, window_len)

        return max_len


if __name__ == "__main__":
    sol = Solution()
    print(sol.characterReplacement("ABAB", 2))     # 4
    print(sol.characterReplacement("AABABBA", 1))  # 4
