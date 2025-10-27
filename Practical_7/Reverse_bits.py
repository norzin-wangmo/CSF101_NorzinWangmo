def reverseBits(n):
    result = 0
    for i in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result
# Time Complexity: O(1)
# Space Complexity: O(1)
# since the number of bits is fixed (32 bits).  
# Example usage:
solution = reverseBits(43261596)
print(solution)  # Output: 964176192
solution = reverseBits(4294967293)
print(solution)  # Output: 3221225471
solution = reverseBits(0)
print(solution)  # Output: 0