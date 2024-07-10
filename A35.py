class Animal:
    def move(self):
        print("Animal moves")

class Dog(Animal):
    def move(self):
        print("Dog runs")

class GermanShepherd(Dog):
    def make_sound(self):
        print("Bark!")

german_shepherd = GermanShepherd()
german_shepherd.make_sound()  # Output: Bark!
