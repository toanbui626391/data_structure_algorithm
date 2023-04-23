"""
strategy to solve the problem
    problem:
        find all unique combinations in candidates where combination sum to target
        each number use one
        possible duplicates in canidate
    why:
        dfs(i, container, total)
            i (int): index of element
            container (list): a combination
            total: sum of current combination
        sort numbs to know where is duplicates in candidates
        if duplicates skip it
"""
from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(i, container, total):
            #base base
            if total == target:
                res.append(container[:]) #res is global, deep copy container
                return
            #stop search
            if i >= len(candidates) or total > target:
                return
            prev = None
            for i in range(i, len(candidates)):
                if candidates[i] == prev: #skip consider duplicate subTree, have to use condition with prev
                    continue
                container.append(candidates[i])
                dfs(i+1, container, total + candidates[i])
                prev = candidates[i]
                container.pop()
        
        res, container = [], []
        candidates.sort()
        dfs(0, container, 0)
        return res