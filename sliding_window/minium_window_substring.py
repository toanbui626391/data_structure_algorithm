#strategy to solve the problem
    #goal:
        # return the minimum window  substring of s such that every character in t (including duplicates) is included in the window
    #why:
        #using sliding window because this is a compare two counter problem. we compare letter between substring of s and string t
        #
    #variables:
        #counter_t, counter_window: to count number of letter in t and window
        #have, need (int): number of key match we have in window vs number of key in counter_t
        #res [l, r]: to keep the index of left and right of substring
        #res_len (float): to keep the length of current substring

from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        counter_t, counter_window = Counter(t), Counter()

        have, need = 0, len(counter_t) #
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            counter_window[c] += 1

            if c in counter_t and counter_window[c] == counter_t[c]:
                have += 1

            while have == need:
                # update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # pop from the left of our window
                counter_window[s[l]] -= 1
                if s[l] in counter_t and counter_window[s[l]] < counter_t[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""

