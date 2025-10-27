def isValid(s: str) -> bool:
    stack = []
    bracket_map = {")": "(", "}": "{", "]": "["}
    
    for char in s:
        if char in bracket_map:  # it's a closing bracket
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
        else:  # it's an opening bracket
            stack.append(char)
    
    return len(stack) == 0
# Time Complexity: O(n)
# Space Complexity: O(n)
# where n is the length of the input string s.
# Example usage:
print(isValid("()"))          # Output: True
print(isValid("()[]{}"))      # Output: True
print(isValid("(]"))         # Output: False
print(isValid("([)]"))       # Output: False
print(isValid("{[]}"))       # Output: True 