"""
Given a string of digits s, return the number of
ways to decode it into letters (A=1, B=2, ..., Z=26).

Example:
  Input:  s="226"
  Output: 3  ("BZ","VF","BBF")

Constraints:
  Each position has at most two valid decodings.
  It can be decoded as a single digit or a pair.
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        # Return 0 immediately if the string is empty
        # or starts with '0'.
        if not s or s[0] == "0":
            return 0

        n = len(s)
        # Maintain only two variables instead of a
        # full array to optimize space to O(1).
        prev2 = 1
        prev1 = 1

        # Iterate over the string from the second
        # character to the end.
        for i in range(2, n + 1):
            current = 0

            # Extract the single digit ending at the
            # current position.
            one_digit = int(s[i - 1:i])

            # Extract the two-digit number ending
            # at the current position.
            two_digits = int(s[i - 2:i])

            # If the single digit is valid, add the
            # decoding ways from the previous step.
            if 1 <= one_digit <= 9:
                current += prev1

            # If the two digits form a valid character,
            # add ways from two steps back.
            if 10 <= two_digits <= 26:
                current += prev2

            # Shift the variables forward for the
            # next mathematical iteration.
            prev2 = prev1
            prev1 = current

        # The final answer is stored in prev1.
        return prev1


if __name__ == "__main__":
    solver = Solution()

    test_1 = "12"
    result_1 = solver.numDecodings(test_1)
    # Expected: 2
    print(f"Input: {test_1} | Output: {result_1}")

    test_2 = "226"
    result_2 = solver.numDecodings(test_2)
    # Expected: 3
    print(f"Input: {test_2} | Output: {result_2}")

    test_3 = "06"
    result_3 = solver.numDecodings(test_3)
    # Expected: 0
    print(f"Input: {test_3} | Output: {result_3}")
