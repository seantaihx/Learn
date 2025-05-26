# Class Practice - Covers Everything

# 1. Create a parent class
class Animal:
    species = "Unknown"  # class variable

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return "Some sound"

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def __repr__(self):
        return f"Animal(name='{self.name}', age={self.age})"

    @staticmethod
    def info():
        return "Animals are living beings."

    @classmethod
    def get_species(cls):
        return cls.species


# 2. Create a child class
class Dog(Animal):
    species = "Canine"  # overrides class variable

    def __init__(self, name, age, breed):
        super().__init__(name, age)  # use parent __init__
        self.breed = breed

    def speak(self):  # override method
        return "Woof!"

    def full_description(self):
        return f"{self.name} is a {self.age}-year-old {self.breed}"


# 3. Practice
d = Dog("Buddy", 5, "Labrador")

# __str__ and __repr__
print(d)             # uses __str__
print(repr(d))       # uses __repr__ from parent

# instance method
print(d.speak())     # overridden in Dog
print(d.full_description())  # method in child

# class method and static method
print(Dog.get_species())     # uses Dog's class variable
print(Dog.info())            # static method

# access instance variables
print(d.name, d.age, d.breed)

# delete a property
del d.age
# print(d.age)  # will error if uncommented

# delete the object
del d
# print(d)  # will error if uncommented
