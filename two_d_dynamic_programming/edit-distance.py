"""
Given two strings word1 and word2, return the
minimum number of operations (insert, delete,
replace) to convert word1 to word2.

Example:
  Input:  word1="horse", word2="ros"
  Output: 3

Constraints:
  Memoized recursion at each (i,j) tries all three operations.
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def get_result(idx1, idx2):
            if idx1 == len(word1) and idx2 == len(word2):
                return 0
            # Only insertions remain when word1 is exhausted.
            if idx1 == len(word1):
                return len(word2) - idx2
            # Only deletions remain when word2 is exhausted.
            if idx2 == len(word2):
                return len(word1) - idx1

            if (idx1, idx2) not in memo:
                if word1[idx1] == word2[idx2]:
                    answer = get_result(idx1 + 1, idx2 + 1)
                else:
                    insert = 1 + get_result(idx1, idx2 + 1)
                    delete = 1 + get_result(idx1 + 1, idx2)
                    replace = 1 + get_result(idx1 + 1, idx2 + 1)
                    answer = min(insert, delete, replace)
                memo[(idx1, idx2)] = answer
            return memo[(idx1, idx2)]

        return get_result(0, 0)
