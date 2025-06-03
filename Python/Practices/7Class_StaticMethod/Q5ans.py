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

employee = Employee()
manager = Manager()

employee.info()
manager.info()


'''SAMPLE OUTPUT
@seantaihx ➜ .../Practice/Python/Practices/7Class_StaticMethod (main) $ python Q5ans.py
Base employee info
Base employee info
Manager info
@seantaihx ➜ .../Practice/Python/Practices/7Class_StaticMethod (main) $ 
'''