"""
strategy to solve the problem
    why:
        using dfs(i, cur, total)
            i is the index of element in candiates which is consider
            cur: the current element in consider
            total: the current sum value in consider
        combination: we can choose the same element multiple time to form a combination
        

"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            #base case
            if total == target:
                res.append(cur.copy())
                return
            #base case to stop recursion
            if i >= len(candidates) or total > target:
                return
            #add element, and continue add that element
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i]) #choose the same element multiple time
            #do not add element and continue with next element
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res