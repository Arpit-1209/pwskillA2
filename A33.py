class Animal:
    def move(self):
        print("Animal moves")

class Dog(Animal):
    def move(self):
        print("Dog runs")

dog = Dog()
dog.move()  # Output: Dog runs
