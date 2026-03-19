"""
Given an integer array nums and an integer k,
return the k most frequent elements. You may
return the answer in any order.

Example:
  Input:  nums=[1,1,1,2,2,3], k=2
  Output: [1,2]

Constraints:
  Bucket sort by frequency avoids a heap for O(n).
"""

from collections import Counter


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = Counter(nums)
        # Index represents frequency; avoids sorting.
        freq = [[] for i in range(len(nums) + 1)]

        # Place each value into the bucket for its count.
        for value, frequency in counter.items():
            freq[frequency].append(value)

        # Collect from the highest-frequency buckets first.
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for element in freq[i]:
                result.append(element)
                if len(result) == k:
                    return result
