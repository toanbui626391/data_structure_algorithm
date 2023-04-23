"""
strategy to solve the problem
    problem: given string s, partition s so that partition is palindrome
    why:
        dfs(i):
            i (int): is the index of current position tree
            j (int): index for all possible partition or subTree
            part (list): to collect valid partition of the current node through the deepth of the depth of the tree
            res (list): collect part when reach the end of the tree

"""
from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def dfs(i):
            if i >= len(s):
                res.append(part[:])
                return
            for j in range(i, len(s)): #j is  possible partition given current 
                if self.isPali(s, i, j):
                    part.append(s[i : j + 1]) #have to include j index
                    dfs(j + 1) #subTree is remaininng string (j+1)
                    part.pop()

        dfs(0)
        return res
    #check is palindrome
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True