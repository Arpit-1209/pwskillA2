from functools import reduce

numbers = [1, -2, 3, -4, 5]
positive_product = reduce(lambda x, y: x * y, filter(lambda x: x > 0, numbers))
print(positive_product)  # Output: 15
