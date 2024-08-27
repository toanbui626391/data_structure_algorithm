class Solution:
    def reverse(self, x: int) -> int:
        resp = 0
        #to handle sign of integer
        sign = 1 if x >= 0 else -1

        int_max_value = 1 << 31 #or 2^31, 2^31-1 is max valid 32 int value
        MAX_VALUE_RES = int_max_value // 10 # max int if remove last degit
        MAX_VALUE_REMAINDER = int_max_value % 10 # last degit value 

        x = abs(x) #remove sign
        while x > 0:
            remainder = x % 10

            if resp > MAX_VALUE_RES or (resp == MAX_VALUE_RES and remainder > MAX_VALUE_REMAINDER):
                return 0

            resp = (resp*10) + (x % 10)
            x //= 10

        return resp * sign