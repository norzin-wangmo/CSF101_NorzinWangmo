def lengthOfLongestSubstring(s):
    char_index = {}
    max_length = 0
    start = 0
    
    for end, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        else:
            max_length = max(max_length, end - start + 1)
        
        char_index[char] = end
    
    return max_length
# Time Complexity: O(n)
# Space Complexity: O(min(m, n))
# where n is the length of the input string s and m is the size of the character set.
# Example usage:
solution = lengthOfLongestSubstring("abcabcbb")
print(solution)  # Output: 3
solution = lengthOfLongestSubstring("bbbbb")
print(solution)  # Output: 1
solution = lengthOfLongestSubstring("pwwkew")
print(solution)  # Output: 3    