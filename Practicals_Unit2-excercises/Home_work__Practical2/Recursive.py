# Recursive Fibonacci function
# fibonacci 0 1 1 2 3 5 8 13 21
def fibonacci_recursive(n):
    """Return the nth Fibonacci number using recursion."""
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Example
num = 6
print(f"Recursive: Fibonacci({num}) =", fibonacci_recursive(num))
