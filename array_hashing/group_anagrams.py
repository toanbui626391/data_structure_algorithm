"""
Given an array of strings strs, group the
anagrams together. You can return the answer
in any order.

Example:
  Input:  strs=["eat","tea","tan","ate","nat","bat"]
  Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Constraints:
  Anagrams share the same sorted character sequence.
"""


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    # Plain dict with setdefault avoids defaultdict.
    collector: dict[str, list[str]] = {}

    for word in strs:
        # Sorting produces a canonical key for anagrams.
        key = "".join(sorted(word))
        collector.setdefault(key, []).append(word)

    return list(collector.values())


if __name__ == "__main__":
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    # Expected: [["eat","tea","ate"],["tan","nat"],["bat"]]
    print(groupAnagrams(words))
