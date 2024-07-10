numbers = [1, 2, 3, 4, 5, 6]
even_squares = list(map(lambda x: x * x, filter(lambda x: x % 2 == 0, numbers)))
print(even_squares)  # Output: [4, 16, 36]
