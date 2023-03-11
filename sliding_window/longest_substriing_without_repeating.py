#strategy to solve the problem
    #goal:

    #why
        #because substring have to be not repeating we have to find the way to keep unique set of char and the index of the last char without repeating
        #char_set (set): to keep the unique subset of the string
        #they key is remove all element on the left untill there are no repeat of the right

#reference solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet: #shift the left until remove left repeated char
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res