class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __str__(self):
        return f"{self.name} is a {self.breed}"

# With __str__ defined
dog1 = Dog("Buddy", "Golden Retriever")
print(dog1)  # This will print: Buddy is a Golden Retriever




'''
Without __str__ (comment it out to test)
def __str__(self):
    return f"{self.name} is a {self.breed}"

Then print(dog1) would show something like:
<__main__.Dog object at 0x000001AB2345>
'''
