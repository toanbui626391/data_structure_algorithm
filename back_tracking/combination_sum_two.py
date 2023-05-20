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
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, com = [], []
        candidates.sort()

        def dfs(i, com, total):
            #base case
            if total == target:
                res.append(com[:])
                return
            if total > target or i > len(candidates):
                return

            #normal case
            prev = None #init prev with None
            for j in range(i, len(candidates)):
                if candidates[j] == prev:
                    continue
                com.append(candidates[j])
                dfs(j+1, com, total+candidates[j])
                prev = candidates[j]
                com.pop()

        dfs(0, com, 0)
        return res