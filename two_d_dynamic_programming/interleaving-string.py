class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        #check for required condition
        if len(s1)+len(s2)!=len(s3):
            return False
        @cache
        def solve(i,j):
            #return True when finish traverse the tree
            if i== len(s1) and j==len(s2):
                return True
            #explor s1 path
            if  i <len(s1) and s3[i+j]==s1[i] and solve(i+1,j):
                return True
            #explore s2 path
            if j<len(s2) and s3[i+j]==s2[j] and solve(i,j+1):
                return True
            return False
        return solve(0,0)