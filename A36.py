class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def __init__(self, breed, species="Dog"):
        super().__init__(species)
        self.breed = breed

    def make_sound(self):
        print("Woof!")

dog = Dog(breed="Labrador")
print(dog.species)  # Output: Dog
print(dog.breed)  # Output: Labrador
