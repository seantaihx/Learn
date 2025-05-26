class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} says Woof!")

    def change_name(self, new_name):
        self.name = new_name

    def __str__(self):
        return f"{self.name} is {self.age} years old."

# Create object
my_dog = Dog("Buddy", 3)

# Print original info
print(my_dog)  # Buddy is 3 years old.

# Change attribute using method
my_dog.change_name("Max")
print(my_dog)  # Max is 3 years old.

# Delete the age attribute
del my_dog.age

# Try to print after deletion
try:
    print(my_dog.age)
except AttributeError:
    print("Age attribute has been deleted.")

# Delete the entire object
del my_dog

# Try to use object after deletion
try:
    print(my_dog)
except NameError:
    print("my_dog no longer exists.")
