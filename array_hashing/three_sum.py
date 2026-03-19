def threeSum(nums: list[int]) -> list[list[int]]:
    res = []
    
    # Step 1: Sort the array (O(n log n) time). 
    # This is required for the two-pointer technique and makes finding duplicates easy.
    nums.sort()
    
    for i in range(len(nums)):
        # Step 2: Skip duplicate 'i' values.
        # If the current number is the same as the previous one, we've already 
        # checked all combinations for this starting number. Move on.
        if i > 0 and nums[i] == nums[i - 1]:
            continue
            
        # Step 3: Set up the two pointers for the remaining array to the right of 'i'
        left = i + 1
        right = len(nums) - 1
        
        # Step 4: The Two-Pointer loop
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            # If the sum is too large, we need a smaller number. Move right pointer left.
            if current_sum > 0:
                right -= 1
                
            # If the sum is too small, we need a bigger number. Move left pointer right.
            elif current_sum < 0:
                left += 1
                
            # We found a valid triplet that equals 0!
            else:
                res.append([nums[i], nums[left], nums[right]])
                
                # Step 5: Skip duplicate 'left' values.
                # We must move the left pointer to find new potential pairs for the same 'i',
                # but we need to ensure we don't land on the exact same number we just used.
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                    
                # Note: We don't strictly need a while-loop to skip 'right' duplicates here 
                # because shifting 'left' to a new number guarantees the sum will change anyway, 
                # naturally forcing 'right' to move in the next iteration of the main while-loop.

    return res