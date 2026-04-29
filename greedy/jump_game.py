def canJump(nums):
    # Keep track of the furthest index we can currently reach
    max_reachable = 0
    
    for i in range(len(nums)):
        # If our current position is beyond the furthest we could ever reach, we're stuck
        if i > max_reachable:
            return False
            
        # Update the furthest we can reach from this new step
        max_reachable = max(max_reachable, i + nums[i])
        
        # Optimization: If we can already reach the end, no need to keep checking
        if max_reachable >= len(nums) - 1:
            return True
            
    return True