class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []
    
# Time Complexity: O(n)
# Space Complexity: O(n)
# where n is the number of elements in the input list nums.
# Example usage:
solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(solution.twoSum([3, 2, 4], 6))    # Output: [1, 2]
print(solution.twoSum([3, 3], 6))       # Output: [0, 1]    