"""
strategy to solve the problem
    problem: find all subsets of a given list
        in subset, position of element is not considered. Example, [1,2] is the same as [2,1]
    why:
        we can draw decision to add or not add element decision tree to solve this problem
        using dfs:
            values (list): glocal varialbes to collect element in the subset
            res: to collectt subsets
"""
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #base case
        def dfs(i):
            #base case
            if i >= len(nums):
                res.append(values[:]) #deep copy
                return
            #add elements    
            values.append(nums[i])
            dfs(i+1)
            #not add elements
            values.pop()
            dfs(i+1)

        res, values = [], []
        dfs(0)
        return res