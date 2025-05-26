# Method Override Practice
'''
This practice shows how a child class can override a method from its parent class

Method override: Redefining a method in the child class that already exists in the parent class

If a method is not overridden, the child will use the parent's method
If a method is overridden, the child method replaces the parent version
You can still call the parent method using super()

!!! The method name must match exactly
'''


# No override: child uses parent method
class Animal:
    def speak(self):
        return "Some sound"

class Cat(Animal):
    pass

c1 = Cat()
print(c1.speak())   # Output: Some sound (from parent)


# With override: child redefines method
class Dog(Animal):
    def speak(self):
        return "Woof!"

d1 = Dog()
print(d1.speak())   # Output: Woof! (child overrides)


# Override with super()
class Bird(Animal):
    def speak(self):
        parent_speak = super().speak()
        return parent_speak + " and tweet"

b1 = Bird()
print(b1.speak())   # Output: Some sound and tweet


# Override with extra behavior
class Cow(Animal):
    def speak(self):
        print("Calling parent:")
        print(super().speak())   # call parent
        return "Moo!"

cw1 = Cow()
print(cw1.speak())   # Output: parent sound + Moo!
