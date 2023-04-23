#problem understanding
    #Given an integer array nums and an integer k
    #return the k most frequent elements.
    # You may return the answer in any order.

#strategy to solve problem:
    #count (hash): to count number of element happend
    #freq (list of list): 
        #index is all possible frequent of element. len(nums) + 1   
        #element (list): all element which happend index frequent  
        #list of list to solve the problem of two element happend the same time
    #res (list): to build response result
        #because freq is to hold all possible frequent we have to loop throug it to collect value
        #stop when we have collect all value

#note about list extend() vs append:
    # append will treat a list as one element
    # extend will extend and treat a list as multiple elemnt

###################################reference solution
from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        counter = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]

        #build freq
        for v, f in counter.items():
            freq[f].append(v)

        #build res
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for e in freq[i]:
                res.append(e)
                if len(res) == k:
                    return res