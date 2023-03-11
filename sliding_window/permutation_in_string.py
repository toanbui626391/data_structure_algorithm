class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sorted_s1 = sorted(s1)
        s1_len = len(s1)
        s2_len = len(s2)
        if len(s1) > len(s2):
            return False
        else:
            for l in range(s2_len - s1_len+1):
                if sorted_s1 == sorted(s2[l:l+s1_len]):
                    return True
        return False
    
###############################################reference solution 2
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26
    
##############################################reference solution v3
#strategy to solve the problem
    #

    #why:
        #using two pointer strategy
    #variables:
        #counter: to keep track of number of element of sustring compare the original string
        #matched: to count map
        #i, i-len(s1) (int): to keep track of left pointer and right pointer of the window
            #right pointer will + matched
            #left pointer will - match
            #they work together compute and update the match of the current window
            
#solution 3 is better than solution one because it reduce sort every time compare a window in s2 string
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #counter to compute the different between current window with the origin string
        cntr, w, matched = Counter(s1), len(s1), 0   

        for i in range(len(s2)):
            if s2[i] in cntr: #right pointer
                cntr[s2[i]] -= 1
                if cntr[s2[i]] == 0:
                    matched += 1
            if i >= w and s2[i-w] in cntr:  #left pointer
                if cntr[s2[i-w]] == 0:
                    matched -= 1
                cntr[s2[i-w]] += 1

            if matched == len(cntr):
                return True

        return False