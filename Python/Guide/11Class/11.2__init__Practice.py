class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")

# Create an object with a name
my_dog = Dog("Buddy")

# Call a method
my_dog.bark()
