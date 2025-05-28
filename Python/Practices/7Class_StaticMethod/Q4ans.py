'''
Create a class Circle with a private attribute _radius.
	•	Use @property to get the radius and compute the area.
	•	Use @radius.setter to safely update _radius.
 '''


class Circle:
    def __init__(self, radius):
        self._radius = radius  # Private-like attribute

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            print("Radius cannot be negative.")
        else:
            self._radius = value

    @property
    def area(self):
        return 3.1416 * (self._radius ** 2)
