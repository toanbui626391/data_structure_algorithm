"""
strategy to solve the problem:
    problem: given a list of number nums which may contains duplicate values. Find all subset of list nums which do not contain duplicate
    why:
        because nums may contains duplicates therefor to avoid duplicate in subsets we have to consider to skip duplicate element in case of not choosing first element of duplicates
        because not choosing first element of duplicate is the same problem of it's parent node
        using dfs(i, subseet) just like subset problem but when we decide not to add, we not add consider that same element
"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::])
                return

            # All subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
            # All subsets that don't include nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res