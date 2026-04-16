class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def countFromCenter(left: int, right: int) -> int:
            count = 0
            # Expand outwards as long as we are in bounds and characters match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1    # Found a palindrome!
                left -= 1     # Expand left
                right += 1    # Expand right
            return count

        total_palindromes = 0
        
        for i in range(len(s)):
            # Add odd-length palindromes centered at i
            total_palindromes += countFromCenter(i, i)
            
            # Add even-length palindromes centered at i and i+1
            total_palindromes += countFromCenter(i, i + 1)
            
        return total_palindromes