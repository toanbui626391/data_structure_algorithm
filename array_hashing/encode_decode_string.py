"""
Problem: Encode and Decode Strings

Encode a list of strings to a single string.
Decode that string back to the original list.

Example:
  Input:  ["lint","code","love"]
  Encoded: "4#lint4#code4#love"

Approach: Length Prefixing
  - Prefix each string with `length` + `#`.
  - When decoding, read digits until `#` to find
    the exact length of the upcoming string.
"""

from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        # Prefix length lets decode find boundaries
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            # Scan forward to find the delimiter '#'
            while s[j] != "#":
                j += 1
                
            length = int(s[i:j])
            
            # The actual substring starts after '#'
            start = j + 1
            end = start + length
            res.append(s[start:end])
            
            # Advance pointer to next encoded string
            i = end
            
        return res
