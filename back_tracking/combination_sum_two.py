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
        candidates.sort()

        res = []

        def backtrack(cur, pos, target):
            if target == 0:
                res.append(cur.copy())
                return
            if target <= 0:
                return

            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                backtrack(cur, i + 1, target - candidates[i])
                cur.pop()
                prev = candidates[i]

        backtrack([], 0, target)
        return res