class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} says Woof!")

    def change_name(self, new_name):
        self.name = new_name

    @staticmethod
    def info():
        print("Dogs are loyal animals.")

    def __str__(self):
        return f"{self.name} is {self.age} years old."

# Create object
my_dog = Dog("Rocky", 4)

# Call instance method
my_dog.speak()        # Rocky says Woof!

# Call static method (no self)
Dog.info()            # Dogs are loyal animals.

# You can also call static method from an object
my_dog.info()         # Dogs are loyal animals.

# Print object
print(my_dog)         # Rocky is 4 years old.
