def twoSum(nums: list[int], target: int) -> list[int]:
    # Dictionary to store the values we've seen and their exact indices.
    # Format: {number: index}
    seen = {}
    
    # enumerate() gives us both the index (i) and the value (num) at the same time
    for i, num in enumerate(nums):
        # Calculate what number we need to hit the target
        complement = target - num
        
        # Check if we have already seen that required number
        if complement in seen:
            # If yes, return the index of the complement and our current index
            return [seen[complement], i]
            
        # If not, add the current number and its index to our dictionary
        # so it can be found by future numbers
        seen[num] = i
        
    # Return an empty list if no match is found
    # (Note: LeetCode usually guarantees exactly one valid solution)
    return []