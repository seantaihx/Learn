# __repr__() Practice
'''
This practice will show how __repr__() works and how it is different from __str__()

__repr__(): Developer-readable representation of object
__str__(): User-readable version of object

If only __repr__() is defined → both print() and repr() will use it
If both are defined:
  - print(object) uses __str__()
  - repr(object) or just typing object in console uses __repr__()
'''


# Only __repr__ defined
class Dog1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Dog1(name='{self.name}', age={self.age})"

d1 = Dog1("Buddy", 5)
print(d1)         # use __repr__() because __str__ not defined
print(repr(d1))   # use __repr__()


# Both __str__ and __repr__ defined, with different outputs
class Dog2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Dog2(name='{self.name}', age={self.age})"

    def __str__(self):
        return f"{self.name} is {self.age} years old"

d2 = Dog2("Max", 3)
print(d2)         # use __str__()
print(repr(d2))   # use __repr__()


# Both defined, but __str__ calls __repr__ to reuse it
class Dog3:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Dog3(name='{self.name}', age={self.age})"

    def __str__(self):
        return self.__repr__()

d3 = Dog3("Charlie", 4)
print(d3)         # same as repr(d3)
print(repr(d3))   # same output
