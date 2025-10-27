def climbStairs(n):
    if n <= 2:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]
# Time Complexity: O(n)
# Space Complexity: O(n)
# where n is the number of stairs.
# Example usage:
solution = climbStairs(5)
print(solution)  # Output: 8
solution = climbStairs(10)
print(solution)  # Output: 89
