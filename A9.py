def generate_powers_of_two(n):
    power = 1
    while power <= n:
        yield power
        power *= 2

for power in generate_powers_of_two(32):
    print(power)  # Output: 1 2 4 8 16 32
