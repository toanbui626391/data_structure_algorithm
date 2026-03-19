"""
Given a string of digits s, return the number of
ways to decode it into letters (A=1, B=2, ..., Z=26).

Example:
  Input:  s="226"
  Output: 3  ("BZ","VF","BBF")

Constraints:
  Each position has at most two valid decodings: single or pair.
"""

from functools import cache


class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def dfs(sub_string):
            # Empty string means a valid decoding was completed.
            if not sub_string:
                return 1
            first_case = 0
            second_case = 0
            # Decode one character if it is 1-9.
            if 1 <= int(sub_string[:1]) <= 9:
                first_case = dfs(sub_string[1:])
            # Decode two characters if they form 10-26.
            if 10 <= int(sub_string[:2]) <= 26:
                second_case = dfs(sub_string[2:])
            return first_case + second_case

        return dfs(s)
