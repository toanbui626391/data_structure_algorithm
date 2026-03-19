"""
Given an array nums of distinct integers, return
all possible permutations.

Example:
  Input:  nums=[1,2,3]
  Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Constraints:
  DFS with a used-array ensures each element appears exactly once.
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def dfs(nums):
            result_local = []

            # Base case: only one element left to place.
            if len(nums) == 1:
                return [nums[:]]

            for i in range(len(nums)):
                # Remove the chosen element from remaining options.
                chosen = nums.pop(0)
                perms = dfs(nums)

                # Append the chosen element to each child permutation.
                for perm in perms:
                    perm.append(chosen)

                result_local.extend(perms)
                # Restore element for the next iteration.
                nums.append(chosen)
            return result_local

        return dfs(nums)
