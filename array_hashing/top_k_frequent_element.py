"""
Problem: Top K Frequent Elements

Given an integer array nums and an integer k,
return the k most frequent elements.

Example:
  Input:  nums=[1,1,1,2,2,3], k=2
  Output: [1,2]

Approach 1: Bucket Sort (O(N) Time)
  - Group numbers into buckets where the bucket
    index equals their frequency.

Approach 2: Min-Heap (O(N log K) Time)
  - Keep a heap of size K of the most frequent.
"""

from typing import List
import heapq

class Solution:
    def topKFrequent(
        self, nums: List[int], k: int
    ) -> List[int]:
        
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            
        # BUCKET SORT APPROACH (O(N))
        freq = [[] for _ in range(len(nums) + 1)]
        for num, c in count.items():
            freq[c].append(num)
            
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res

    def topKFrequent_heap(
        self, nums: List[int], k: int
    ) -> List[int]:
        
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            
        # HEAP APPROACH (O(N log K))
        return heapq.nlargest(
            k, count.keys(), key=lambda x: count[x]
        )
