#problem understanding
    #encode with length of string and #
        #length of string to find the end index of string in encoded string
        # # to mark starting index and ending index of string
        
#strategy to solve the problem
    #we can not use other data structure to store information about encoded string
    #we store lenght of string and mark string seperation by #
    # variable:
        #i (int) to keep track of the end index of string
        #j (int) to keep track of the start (or position of # of the current string)

##########################################reference solution
class Solution:


    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res 

    """
    @param: s: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, s):
        res, i = [], 0 #i to keep track of end index of string
        while i < len(s):
            j = i 
            while s[j] != "#":
                j += 1 #j to keep track of # position related to the current string
            length = int(s[j - 1])
            res.append(s[(j+1):(j+1+length)])
            i = j+1+length
        return res