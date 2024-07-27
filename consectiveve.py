def findMaxConsecutiveOnes(nums):
    max_consecutive = 0
    current_consecutive = 0
    
    for num in nums:
        if num == 1:
            current_consecutive += 1
        else:
            if current_consecutive > max_consecutive:
                max_consecutive = current_consecutive
            current_consecutive = 0
    
    # Final check in case the array ends with a streak of 1's
    if current_consecutive > max_consecutive:
        max_consecutive = current_consecutive
    
    return max_consecutive

# Test cases
print(findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))  # Output: 3
print(findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))  # Output: 2
