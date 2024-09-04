class Solution:
    def isHappy(self, n: int, visited=None) -> bool:
        # Check if the visited set is None
        if visited is None:
            visited = set()  # Create an empty set to store visited numbers
    
        if n == 1:
            return True
        
        if n in visited:
            return False
        
        visited.add(n)  # Add n to the visited set
        
        # Calculate the new number by summing the squares of the digits
        new_num = sum(int(digit) ** 2 for digit in str(n))
        
        # Recursively call isHappy with the new number and the updated visited set
        return self.isHappy(new_num, visited)