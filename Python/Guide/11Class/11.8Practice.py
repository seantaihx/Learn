class Dog:
    species = "Canis familiaris"  # Class variable

    def __init__(self, name, age):
        self.name = name          # Instance variable
        self.age = age

    def speak(self):
        print(f"{self.name} says Woof!")  # Instance method

    def change_name(self, new_name):
        self.name = new_name      # Changing attribute

    @staticmethod
    def info():
        print("Dogs are loyal animals.")  # Static method

    @classmethod
    def show_species(cls):
        print(f"All dogs belong to: {cls.species}")  # Class method

    def __str__(self):
        return f"{self.name} is {self.age} years old."  # __str__ method


# Create object
dog1 = Dog("Buddy", 3)

# Instance methods
dog1.speak()              # Buddy says Woof!
dog1.change_name("Max")
print(dog1)               # Max is 3 years old.

# Static method
Dog.info()                # Dogs are loyal animals.

# Class method
Dog.show_species()        # All dogs belong to: Canis familiaris
