'''
Create a base class Employee with a method info() that prints "Base employee info".
	•	Create a subclass Manager that overrides info() but also calls super().info() before printing "Manager info".
'''


class Employee:
    def info(self):
        print("Base employee info")

class Manager(Employee):
    def info(self):
        super().info()  # Call the parent method first
        print("Manager info")
