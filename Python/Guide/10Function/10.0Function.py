#Function
'''
Some pre-written code that may be used for multiple times, so we dont need to keep repeating those code

Pure Function: Always give the same results if input are the same

Impure Function: Depends on any external state that would modify/affect the output

return statement: Return a value or statement and ends the function immediately

scope: a variable is only available from inside the region it's created.
If a variable is created inside a function, it cannot be used outside the function
If it was created outside of every function, it can be used everywhere
'''

#Scope
'''
Global keyword: make the variable become globally available
format:
global x
x = 300

non-local keyword: make the variable in inner function become accessible in the outer function
format:
non-local x
x = 300
'''


#Custom Function
'''
We can define our own custome function

format:
def function_name(parameter1(optional), parameter(optional2), ...):
    code

the parameter is what will be used inside the code, and may be modified, or just for reading

if want to return a value
def function_name(parameter1(optional), parameter(optional2), ...):
    code
    return statement
!!! return a, b will return a tuple

if want to have default value for parameter
def function_name(parameter1 = default_value1, ..):
    statement

if unknown number of parameter, add * before parameter_name when defining
def function_name(*parameter1, ...):
    statement

if want a keyword only argument
def function_name(*, parameter):
    statement

if want a position argument
def function_name(parameter1, /):
    statement
'''

#*args and **kwargs
'''
while defining a function, if we dont know how many argument there will be, we can use *args as argument
to differentiate if the argument is inside the *args or not, we can use **kwargs as argument when defining

*args: tell the function to treat all the positional arguments as a tuple
**kwargs: keyword-only (variable = value)

positional-only argument: only value
keyword-only argument: variable = value

Or we can be like
1. def func(a, *, b, c):     => everything after * is keyword-only
2. def func(a, b, /):        => everything before / is positional-only
3. def func(a, b, /, c, *, d, e):     => the first two argument is positional only, extra positional value belongs to c, d and e is keyword only

!!!/ must come BEFORE any * while * come AFTER any /
'''


#Recursion
'''
Function that calls itself

format:
def function_name(parameter):
    statement
    condition:
        function(parameter with counter)

'''


#Special Function Lambda
'''
This is an anonymous function (function without name) and is quick to create and use

format: lambda parameter: expression
'''


#Map() Function
'''
Applies a specified function to every element in an iterable

format: map(function, iterable)
'''

#Filter() Function
'''
Apply a condition specified in the provided function to each item in iterable and return only those which function evaluates to True

format: filter(function, iterable)
'''

#Outer and Inner Function
'''
Inner function is a function inside a function while outer function is a function with a function inside of it

format:
def func_out(outer_arg):
    statement
    def func_in(in_arg):
        statement
        return sth
    return func_in(in_arg)
'''


#@Decorator
'''
@Decorator: Use function below as argument of function of decorator

format:
@func

def function(func):
    statement
    (use func function inside)
    return

@function
def function2():
    return...
'''


#
'''
We can use if __name__ == "__main__":
this is to see if the current file is the where the main function and custom functions are

or just main() at the end
'''



