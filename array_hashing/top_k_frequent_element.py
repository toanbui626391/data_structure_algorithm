#problem understanding
    #Given an integer array nums and an integer k
    #return the k most frequent elements.
    # You may return the answer in any order.

#strategy to solve problem:
    #count (hash): to count number of element happend
    #freq (list of list): 
        #index is all possible frequent of element   
        #element (list): all element which happend index frequent  
    #res (list): to build response result
        #because freq is to hold all possible frequent we have to loop throug it to collect value
        #stop when we have collect all value

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
        for q, v in counter.items():
            freq[v].append(q)

        #build res
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for e in freq[i]:
                res.append(e)
                if len(res) == k:
                    return res