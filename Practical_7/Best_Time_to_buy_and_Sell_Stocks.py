def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit

# Time Complexity: O(n)
# Space Complexity: O(1)
# where n is the number of days (length of the input list prices).
# Example usage:
solution = maxProfit([7, 1, 5, 3, 6, 4])
print(solution)  # Output: 5
solution = maxProfit([7, 6, 4, 3, 1])
print(solution)  # Output: 0