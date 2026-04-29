def maxSubArray(nums):
    # Initialize both variables with the first element
    current_sum = nums[0]
    max_sum = nums[0]
    
    # Iterate through the rest of the array starting from the second element
    for i in range(1, len(nums)):
        num = nums[i]
        
        # Decide: add to the running sum, or start fresh from 'num'?
        current_sum = max(num, current_sum + num)
        
        # Update the global maximum if our current chunk is the best we've seen
        max_sum = max(max_sum, current_sum)
        
    return max_sum