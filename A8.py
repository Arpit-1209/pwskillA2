def generate_even_numbers(n):
    for i in range(2, n + 1, 2):
        yield i

for even_number in generate_even_numbers(10):
    print(even_number)  # Output: 2 4 6 8 10
