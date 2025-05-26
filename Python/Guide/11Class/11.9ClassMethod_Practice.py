class Dog:
    species = "Canis familiaris"  # Class variable

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} says Woof!")

    @staticmethod
    def info():
        print("Dogs are loyal animals.")

    @classmethod
    def get_species(cls):
        print(f"All dogs belong to: {cls.species}")

    def __str__(self):
        return f"{self.name} is {self.age} years old."

  # Create object
dog1 = Dog("Charlie", 2)

# Instance method
dog1.speak()            # Charlie says Woof!

# Static method
Dog.info()              # Dogs are loyal animals

# Class method
Dog.get_species()       # All dogs belong to: Canis familiaris

# Print object (uses __str__)
print(dog1)             # Charlie is 2 years old

