"""
An Anagram is a word or phrase formed by
rearranging the letters of a different word or
phrase, using all original letters exactly once.
Given two strings s and t, return true if t is
an anagram of s, and false otherwise.

Example:
  Input:  s="anagram", t="nagaram"
  Output: True

Constraints:
  Two anagrams must have the same length.
"""


def isAnagram(s: str, t: str) -> bool:
    # Length mismatch means they cannot be anagrams.
    if len(s) != len(t):
        return False

    # Count character frequencies manually using
    # a plain dict instead of Counter.
    freq_s: dict[str, int] = {}
    freq_t: dict[str, int] = {}

    for char in s:
        freq_s[char] = freq_s.get(char, 0) + 1

    for char in t:
        freq_t[char] = freq_t.get(char, 0) + 1

    # Equal frequency maps confirm anagram relationship.
    return freq_s == freq_t


if __name__ == "__main__":
    # Expected: True
    print(isAnagram("anagram", "nagaram"))

    # Expected: False
    print(isAnagram("rat", "car"))
