'''
Create an abstract base class Shape with an abstract method area().
	•	Create two subclasses: RectangleMixin (with width and height) and PrintableMixin (adds a __repr__() that shows the shape’s dimensions).
	•	Then, create a class PrintableRectangle that inherits from both RectangleMixin and PrintableMixin, and also inherits from Shape.

Finally:
	•	Implement the area() method in PrintableRectangle.
	•	Create an instance of PrintableRectangle, print it, and print its area.
'''

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class RectangleMixin:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class PrintableMixin:
    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class PrintableRectangle(RectangleMixin, PrintableMixin, Shape):
    def __init__(self, width, height):
        super().__init__(width, height)  # Inherits from RectangleMixin

    def area(self):
        return self.width * self.height

# Test
rect = PrintableRectangle(4, 5)
print(rect)        
print(rect.area())   


'''SAMPLE OUTPUT
@seantaihx ➜ .../Practice/Python/Practices/7Class_StaticMethod (main) $ python Q6ans.py
Rectangle(width=4, height=5)
20
@seantaihx ➜ .../Practice/Python/Practices/7Class_StaticMethod (main) $ 
'''