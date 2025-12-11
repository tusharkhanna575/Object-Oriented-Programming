class User:
    def __init__(self, name, age=None):
        self.name = name
        self.age = age

User("Alice")
User("Bob", 30)
