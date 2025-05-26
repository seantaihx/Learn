class Dog:
    def __init__(self, name, age):
        self.name = name      # Instance variable
        self.age = age

    def speak(self):
        print(f"{self.name} says Woof!")

    def __str__(self):
        return f"{self.name} is {self.age} years old."

# Create object
my_dog = Dog("Max", 5)

# Call object method
my_dog.speak()     # Output: Max says Woof!

# Use print to trigger __str__
print(my_dog)      # Output: Max is 5 years old.
