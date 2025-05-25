#Class
'''
Python is an object-oriented programming language, so almost everything in Python is an object, with its properties and methods
Think like

Class = blueprint
Object = actual thing built from the class, also called an instance of the class
'''


#Create a class
'''
format:
class class_name:
  statement

!!!This is the simplest form
'''

#Create an object without storing internal data
'''
format:
class class_name:
  statement
object_name = class_name()

statement(object.value)

!!!This is the simplest form
'''


#Create an object with storing internal data
'''
__init__() function: Class function that always execute when class is being initiated

format:
class class_name:
  def __init__(self, arg1, arg2, ...):
    self.arg1 = value1
    self.arg2 = value2

object = class_name(value1, value2)


To access the value
object.arg1      => value1
object.arg2      => value2
'''


#__str__() function
'''
__str__(): A function in class that controls what should be returned when class object represented as a string
if not set, string representation of the object is returned （something like <__main__.Dog object at 0x7fb2e1e1b5b0>)

format:
class class_name:
  def __init__(self, name, age):
    self.arg1 = value1
    self.arg2 = value2

  def __str__(self):
    return f"{self.arg1}, {self.arg2}"

'''


#Object Methods
'''
Object Method: Method in objects are functions belong to the object

ex:
class person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def func(self):
    print("Hi " + self.name)
  p1 = person("John", 36)
  p1.func()

In this case, func() is object method
'''

