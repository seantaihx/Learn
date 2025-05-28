'''
Create a base class Animal with a method speak().
	•	Create a subclass Dog that overrides speak() to print "Woof!".
	•	Create a Dog object and call speak().
'''

class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")
