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


# __repr__() Function
'''
__repr__(): A special class method that defines how the object is represented as a developer-readable string

When you print an object, Python will try to use __str__()
But if __str__() is not defined, it will use __repr__()

repr(object) will always call __repr__()

Think of __repr__() as:
    - For developers
    - For debugging
    - Shows clear or detailed info about the object
    - Often tries to look like valid Python code to recreate the object

format:
class class_name:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def __repr__(self):
        return f"ClassName(arg1={self.arg1}, arg2={self.arg2})"

object = class_name(value1, value2)

print(repr(object))       => use __repr__()
print(object)             => use __str__() if exists, else use __repr__()
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


#Self Parameter
'''
self parameter: reference to the current instances and is used to access variables that belongs to the class.


!!!Doesnt have to be named self, but have to be the first parameter of function, and also it's recommended to use self
'''


#Del Statement
'''
del statement: used to delete property or delete object

1. delete property: del variable.parameter
ex: del p1.age

2. delete object: del variable
ex: del p1
'''

# Method Override
'''
Method override: When a child class defines a method with the same name as a method in its parent class

Purpose: To change or customize the behavior of the inherited method

Think like:
Parent class gives a general method
Child class wants to do it differently, so it overrides (replaces) the method

!!! Only works if the method names match exactly
!!! super() can still be used to access the parent method if needed

format:
class Parent:
    def greet(self):
        return "Hello from Parent"

class Child(Parent):
    def greet(self):              # This overrides Parent's greet()
        return "Hello from Child"

object = Child()
print(object.greet())     => Hello from Child
'''


#Static Method
'''
static method: very similar to class, but doesnt take the implicit first argument
It is like a regular function but lives in the class's namespace

format:
class class_name:
	statement
  @staticmethod
  def func(arg1, arg2,...):
  		statement
    return statement
    

Use static method when the method logic is related to the class but doesnt need to use class or instance data    


!!!Cant access instance variables and class variables since it doesnt use class or instance data
'''


#Class Method
'''
class method: method that is bound to the class and not the instance, it can access and modify class state using the cls parametr

format:
class class_name:
  	class_variable = value1
    
  @classmethod
  def class_method(cls):
    cls.class_variable 
    
    
Use class method when creating class instances with custom logic, modifying class-level data, or some behaviour that depends on the class especially when subclassing    

'''


#Inheritance
'''
Parent class is class being inherited from, also called base class
Child class is class that inherits from another class, also called derived class

A) To Create A Parent And Child Class
parent: same as creating a class
ex: class parent:

child: use parent class as parameter
ex: class child(parent)


B) Super() Function
Make child class inherit all the methods and properties from its parent

format:
class child(parent):
	def __init__(self, arg1, arg2,...):
 		super().__init__(arg1, arg2)

C) Add Properties
class child(parent):
	def __init__(self, parg1, parg2, carg1):
 		super().__init__(parg1, parg2)
   		self.carg1 = carg1
'''




