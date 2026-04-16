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
        # Initialize an array to store the number of
        # decoding ways for each prefix length.
        dp = [0] * (n + 1)

        # Base cases: an empty string and a string of
        # length 1 have exactly 1 decoding way.
        dp[0] = 1
        dp[1] = 1

        # Iterate over the string from the second
        # character to the end.
        for i in range(2, n + 1):
            # Extract the single digit ending at the
            # current position.
            one_digit = int(s[i - 1:i])

            # Extract the two-digit number ending
            # at the current position.
            two_digits = int(s[i - 2:i])

            # If the single digit is valid, add the
            # decoding ways from the previous step.
            if 1 <= one_digit <= 9:
                dp[i] += dp[i - 1]

            # If the two digits form a valid character,
            # add ways from two steps back.
            if 10 <= two_digits <= 26:
                dp[i] += dp[i - 2]

        # The final answer is stored in the last
        # element of the dp array.
        return dp[n]


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
