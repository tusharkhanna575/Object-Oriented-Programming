class Animal:
    def __init__(self, name):
        self.name = name
        print("Animal constructor")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)      # constructor chaining happens here
        self.breed = breed
        print("Dog constructor")

d = Dog("Buddy", "Labrador")