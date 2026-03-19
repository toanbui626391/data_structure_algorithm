"""
Encode a list of strings to a single string.
Decode that string back to the original list.

The encoding prefixes each string with its length
and a '#' delimiter so decoding is unambiguous.

Example:
  Input:  ["lint","code","love","you"]
  Encoded: "4#lint4#code4#love3#you"
"""


class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        result = ""
        for string in strs:
            # Prefix length lets decode find each string's end.
            result += str(len(string)) + "#" + string
        return result

    """
    @param: s: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, s):
        result = []
        i = 0

        while i < len(s):
            # Find '#' to locate the boundary of the length prefix.
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            result.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return result
