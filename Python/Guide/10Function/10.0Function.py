#Function
'''
Some pre-written code that may be used for multiple times, so we dont need to keep repeating those code

Pure Function: Always give the same results if input are the same

Impure Function: Depends on any external state that would modify/affect the output
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