# Iterative Fibonacci function
# fibonacci 0 1 1 2 3 5 8 13 21
def fibonacci_iterative(n):
    """Return the nth Fibonacci number using iteration."""
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Example
num = 6
print(f"Iterative: Fibonacci({num}) =", fibonacci_iterative(num))