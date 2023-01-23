#problem understand
    #Alphanumeric characters include letters and numbers.
    #when a phrase is conver to all lower case and remove all non-alphnumeric character you can read from left is the same as read from the right

#strategy to solve the problem
    #read from the left is also read from the right. Therefore, we using two point ter
    #have to have machenisum to remove or check for non-alphanumeric
    #we only have to check when l < r or in the middle point
    #variable:
        #l, r (int) to keep stack of position of each pointer
        # l < r is the condition to stop the loop
        # s.isalnum() to check is Alphanumeric character
        # s.lower() to lower case in string method

################################################################reference solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) -1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True