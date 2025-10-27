def missingNumber(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum
# Time Complexity: O(n)
# Space Complexity: O(1)
# where n is the length of the input list nums.
# Example usage:
solution = missingNumber([3, 0, 1])
print(solution)  # Output: 2
solution = missingNumber([0, 1])
print(solution)  # Output: 2
solution = missingNumber([9,6,4,2,3,5,7,0,1])
print(solution)  # Output: 8