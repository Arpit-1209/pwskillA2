numbers = [1, 2, 3, 4, 5]
doubled_odds = list(map(lambda x: x * 2, filter(lambda x: x % 2 != 0, numbers)))
print(doubled_odds)  # Output: [2, 6, 10]
