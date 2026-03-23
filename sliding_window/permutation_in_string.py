"""
Problem: Permutation in String

Given s1 and s2, return True if s2 contains
a permutation of s1 as a contiguous substring.

Example:
  Input:  s1="ab", s2="eidbaooo"
  Output: True

Constraints:
  1 <= len(s1), len(s2) <= 10^4
  s1 and s2 consist of lowercase letters.

Approach: Fixed-size sliding window (size=len(s1))
  - Use frequency maps (dictionaries) to count
    characters.
  - Python tests `dict1 == dict2` in O(1) time
    for small dictionaries (max 26 keys).
  - Cleanest and most idiomatic Python approach.

Complexity:
  Time O(26 * n) -> O(n)
  Space O(26) -> O(1)
"""


class Solution:
    def checkInclusion(
        self, s1: str, s2: str
    ) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        count1 = {}
        for c in s1:
            count1[c] = count1.get(c, 0) + 1

        count2 = {}
        for c in s2[:n1]:
            count2[c] = count2.get(c, 0) + 1

        if count1 == count2:
            return True

        # Slide window one character at a time
        for i in range(n1, n2):
            # Expand window: Add rightmost char
            r_char = s2[i]
            count2[r_char] = count2.get(r_char, 0) + 1

            # Shrink window: Remove leftmost char
            l_char = s2[i - n1]
            count2[l_char] -= 1
            if count2[l_char] == 0:
                del count2[l_char]

            # Compare map directly
            if count1 == count2:
                return True

        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.checkInclusion("ab", "eidbaooo"))
    print(sol.checkInclusion("ab", "eidboaoo"))
    print(sol.checkInclusion("ab", "ab"))
