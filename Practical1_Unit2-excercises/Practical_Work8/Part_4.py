# Reverse a string
def reverse_string(s):
    stack = stack()
    for char in s:
        stack.push(char)

    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string

#Test the function
print(reverse_string("Hello, World!"))  # Should print "!dlroW ,olleH"
