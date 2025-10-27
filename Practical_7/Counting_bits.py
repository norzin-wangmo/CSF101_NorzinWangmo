def countBits(n):
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        ans[i] = ans[i >> 1] + (i & 1)
    return ans
# Time Complexity: O(n)
# Space Complexity: O(n)
# where n is the input integer.
# Example usage:
solution = countBits(5) 
print(solution)  # Output: [0, 1, 1, 2, 1, 2]
solution = countBits(2) 
print(solution)  # Output: [0, 1, 1]
solution = countBits(0) 
print(solution)  # Output: [0]          