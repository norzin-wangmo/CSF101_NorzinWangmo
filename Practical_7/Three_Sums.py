def threeSum(nums):
    results = []
    nums.sort()
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue  # Skip duplicate values for i
        
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                results.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates for left and right
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    
    return results

# Time Complexity: O(n^2)
# Space Complexity: O(k)
# where n is the number of elements in the input list nums and k is the number of unique triplets found.
# Example usage:
solution = threeSum([-1, 0, 1, 2, -1, -4])
print(solution)  # Output: [[-1, -1, 2], [-1, 0, 1]]
solution = threeSum([0, 1, 1])
print(solution)  # Output: []   