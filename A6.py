def generate_squares(n):
    for i in range(1, n + 1):
        yield i * i

for square in generate_squares(5):
    print(square)  # Output: 1 4 9 16 25
