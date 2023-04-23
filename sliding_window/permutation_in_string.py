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
        #counter (Counter): count in reverse to compare the s1 to the current window. counter[char] == 0 then that char is matched
        #we also know len of the window base on len of s1. therefore we can we can decide when to move left pointer base on that.

    #variables:
        #counter (Counter): to count in reverse from s1 to 0. If one key is 0 then that char is matched
        #matched, counter_len (int): to count matched compute to elements in s1. if matched = counter_len then substring is permutation of s1
        #len_s1 (int): len of s1 is also the width of sliding window
        #r, r-len_s1 (int): to keep track of left pointer and right pointer of the window
            #right pointer will + matched
            #left pointer will - match
            #they work together compute and update the match of the current window
            
#solution 3 is better than solution one because it reduce sort every time compare a window in s2 string
            #they work together compute and update the match of the current window
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        counter = Counter(s1)
        matched, counter_len = 0, len(counter)
        len_s1 = len(s1)

        for r in range(len(s2)):

            if s2[r] in counter:
                counter[s2[r]] -= 1
                if counter[s2[r]] == 0:
                    matched += 1

            if r >= len_s1 and s2[r-len_s1] in counter:
                if counter[s2[r-len_s1]] == 0:
                    matched -= 1
                counter[s2[r-len_s1]] += 1

            if matched == counter_len:
                return True

        return False