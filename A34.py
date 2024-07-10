class Animal:
    def move(self):
        print("Animal moves")

class Dog(Animal):
    def move(self):
        print("Dog runs")

class Mammal:
    def reproduce(self):
        print("Giving birth to live young")

class DogMammal(Dog, Mammal):
    pass

dog_mammal = DogMammal()
dog_mammal.reproduce()  # Output: Giving birth to live young
dog_mammal.make_sound()  # Output: Woof!
dog_mammal.move()  # Output: Dog runs
