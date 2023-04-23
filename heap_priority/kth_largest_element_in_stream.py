"""
strategy to solve the problem
    problem: design class which get kth largest element in steam at O(n)
    why:
        using min heap with size kth. because min heap will main tain the smallest element as root. Therefore the kth largest element will be as roots

"""
import heapq
from typing import List
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        #build size kth min heap
        self.k , self.nums = k, nums
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        #push and pop element to maintain size kth
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]