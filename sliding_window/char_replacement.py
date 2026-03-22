"""
Given a string s and an integer k, return the
length of the longest substring containing the
same letter after performing at most k replacements.

Example:
  Input:  s="ABAB", k=2
  Output: 4

Constraints:
  Window is valid when (size - max_char_count) <= k.
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Plain dict; get() returns 0 for unseen keys.
        char_counter: dict = {}
        left = 0
        result = 0
        # Track max frequency to avoid recomputing it each step.
        max_char = 0
        for r in range(len(s)):
            char_counter[s[r]] = (
                char_counter.get(s[r], 0) + 1
            )
            max_char = max(max_char, char_counter[s[r]])
            total_char = r - left + 1
            # Shrink window when replacements needed exceed k.
            if total_char - max_char > k:
                char_counter[s[left]] = (
                    char_counter.get(s[left], 0) - 1
                )
                left += 1
            else:
                result = max(result, total_char)
        return result


if __name__ == "__main__":
    sol = Solution()
    # Expected: 4
    print(sol.characterReplacement("ABAB", 2))
    # Expected: 4
    print(sol.characterReplacement("AABABBA", 1))
