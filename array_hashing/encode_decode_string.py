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

#strategy to solve the problem v2:
    #problem: 
        #encode a list of string into a single string
        #decode string back to original list of string

    #why:
        #we do we need both length and seperator (#) as the start of each string
        # the # will help in decode state to finde the lenght of the current word. because in decode state length is string and we do not know it value
        # we compute length of the current word with index i, j
            #j (int) is the index of # at the current word
            #i (int) is the index of # for the next word
##########################################reference solution
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

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
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j]) # the #seperator will help us find the length of the current word
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res