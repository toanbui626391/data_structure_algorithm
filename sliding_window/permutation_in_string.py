"""
Problem: Permutation in String

Given strings s1 and s2, return True if s2
contains a permutation of s1.
A permutation appears as a contiguous substring
with the same character frequencies.

Example:
  Input:  s1 = "ab", s2 = "eidbaooo"
  Output: True

Constraints:
  1 <= len(s1), len(s2) <= 10^4
  s1 and s2 consist of lowercase letters.

Approach: Fixed-size sliding window of size k
  where k = len(s1).

  - Build frequency maps for s1 (need) and
    the first window of s2 (have).
  - Track how many distinct characters are
    fully matched (need[c] == have[c]).
  - Slide the window one step at a time:
      * Add the new right character.
      * Remove the old left character.
      * Update the matched count.
  - If matched == distinct chars in s1,
    a permutation is found.

Complexity:
  Time  O(n)  one pass over s2
  Space O(1)  at most 26 keys in each map
"""


class Solution:
    def checkInclusion(
        self, s1: str, s2: str
    ) -> bool:
        k = len(s1)
        n = len(s2)

        if k > n:
            return False

        # --- build frequency maps ---
        need = {}
        for ch in s1:
            need[ch] = need.get(ch, 0) + 1

        have = {}
        for ch in s2[:k]:
            have[ch] = have.get(ch, 0) + 1

        # count distinct chars fully matched
        distinct = len(need)
        matched = 0
        for ch in need:
            if have.get(ch, 0) == need[ch]:
                matched += 1

        if matched == distinct:
            return True

        # --- slide the window ---
        left = 0
        for right in range(k, n):

            # expand: add s2[right]
            new_ch = s2[right]
            have[new_ch] = have.get(new_ch, 0) + 1
            if new_ch in need:
                if have[new_ch] == need[new_ch]:
                    matched += 1
                # overshot: one match lost
                elif have[new_ch] == need[new_ch] + 1:
                    matched -= 1

            # shrink: remove s2[left]
            old_ch = s2[left]
            if old_ch in need:
                if have[old_ch] == need[old_ch]:
                    matched -= 1
                # back to exact: one match gained
                elif have[old_ch] == need[old_ch] + 1:
                    matched += 1
            have[old_ch] -= 1
            if have[old_ch] == 0:
                del have[old_ch]
            left += 1

            if matched == distinct:
                return True

        return False


if __name__ == "__main__":
    sol = Solution()

    # True: "ba" at index 1 is a permutation of "ab"
    print(sol.checkInclusion("ab", "eidbaooo"))

    # False: no permutation of "ab" in "eidboaoo"
    print(sol.checkInclusion("ab", "eidboaoo"))

    # True: "ab" itself
    print(sol.checkInclusion("ab", "ab"))

    # False: s1 longer than s2
    print(sol.checkInclusion("abc", "ab"))
