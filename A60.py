import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def calculate_area(cls, radius):
        return math.pi * (radius ** 2)

print(Circle.calculate_area(5))  # Output: 78.53981633974483
