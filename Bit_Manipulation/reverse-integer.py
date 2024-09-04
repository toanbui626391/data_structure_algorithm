class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        #to handle sign of integer
        sign = 1 if x >= 0 else -1

        int_max_value = 1 << 31 #or 2^31, 2^31-1 is max valid 32 int value
        MAX_VALUE_RES = int_max_value // 10 # max int if remove last degit
        MAX_VALUE_REMAINDER = int_max_value % 10 # last degit value 

        x = abs(x) #remove sign
        while x > 0:
            #compute remainder
            remainder = x % 10

            if res > MAX_VALUE_RES or (res == MAX_VALUE_RES and remainder >= MAX_VALUE_REMAINDER):
                return 0

            res , x = (res*10) + (x % 10), x//10

        return res * sign