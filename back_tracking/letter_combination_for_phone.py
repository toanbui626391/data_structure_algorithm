"""
Given a string of digits, return all possible
letter combinations that the digits could represent
on a phone keypad. Return an empty list for "".

Example:
  Input:  digits="23"
  Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Constraints:
  DFS at each digit level adds one character per branch.
"""

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        # Maps digit characters to their keypad letters.
        digit_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(idx, current_string):
            # All digits processed; record the combination.
            if idx == len(digits):
                result.append(current_string)
                return
            for char in digit_to_char[digits[idx]]:
                backtrack(idx + 1, current_string + char)

        if digits:
            backtrack(0, "")

        return result
