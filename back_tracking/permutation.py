"""
strategyt to solve the problem
    problem: list all permutation of a given list of elements
        permutation of n elements is all possible position of that n element. each permutation will have len of n and we consider position of each elements
        permutation do not allow duplicate element
        example of permutation: [1, 2, 3] and [2, 1, 3] are permutation of each other
    why:
        using dfs(used, per)
            used to check element have been add to perm
            per to collect element in permutation
            if used we just skip it

"""

from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(per, used):
            #base case
            if len(per) >= len(nums):
                return res.append(per[:])
            #normal case
            for i in range(len(nums)):
                if used[i]: #permutation do not allow duplicate value
                    continue
                #add element to per
                per.append(nums[i])
                used[i] = True
                dfs(per, used)
                #convert per and used back for next treeNode in the same level
                per.pop()
                used[i] = False
        res, used = [], [False] * len(nums)
        dfs([], used)
        return res


from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(nums):

            res = [] #collector as the current level

            #base case
            if len(nums) == 1:
                return [nums[:]] #return list and deep copy

            for i in range(len(nums)): #possible paths
                n = nums.pop(0) #pop left
                perms = dfs(nums) #call child node

                for perm in perms: #construct perm from child
                    perm.append(n)
                
                res.extend(perms)
                nums.append(n) #append back for next path call
            return res

        return dfs(nums)