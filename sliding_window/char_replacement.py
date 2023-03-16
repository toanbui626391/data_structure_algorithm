#strategy to solve the problem
    #goal: return the length of the longest substring container the same letter after perform k replacement in that substring

    #why:
        #we want the length of longest substring, therefore one possible strategy is sliding window
        #sliding window will try to reach longest substring but we need condition so that it is valid solution
        #we need to know the most comment char and then check is it valid solution if it is not a valid, we update left pointer to check another solution
        #the key is that we also need to update char_counter before we move left pointer

        #find the current max_char by compare the past max_char with the current char count in question
        #it is a valid repeat substring with k replace if total_char (r-l+1) - max_char > k

    #variable:
        #max_char, total_char (int): for each iteration we need to keep track of the current maxium char and total char in the window to decide is this substring a valid repeat substring
        #l, r (int): to keep track of left and right pointer of the current window
        # res (int): to search for the length of longest substring
#########################reference solution
from collections import Counter, defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        char_counter = defaultdict(int)
        for r in range(len(s)):
            char_counter[s[r]] += 1
            if (r-l+1) - max(char_counter.values()) > k:
                char_counter[s[l]] = char_counter[s[l]] - 1
                l += 1
                
            res = max(res, r-l+1)
        return res
    
#############################reference solution
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_counter = Counter()
        l, res = 0, 0
        max_char = 0
        for r in range(len(s)):
            char_counter[s[r]] += 1
            max_char = max(max_char, char_counter[s[r]])
            total_char = r-l+1
            if total_char - max_char > k:
                char_counter[s[l]] -= 1
                l += 1
            else:
                res = max(res, total_char)
        return res
            