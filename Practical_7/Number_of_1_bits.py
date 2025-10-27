def hammingWeight(n: int) -> int:
    count = 0
    while n:
        n &= (n - 1)
        count += 1
    return count
# Time Complexity: O(k)
# Space Complexity: O(1)
# where k is the number of 1 bits in the integer n. 
# Example usage:
solution = hammingWeight(11)
print(solution)  # Output: 3
solution = hammingWeight(128)
print(solution)  # Output: 1
solution = hammingWeight(4294967293)
print(solution)  # Output: 31
