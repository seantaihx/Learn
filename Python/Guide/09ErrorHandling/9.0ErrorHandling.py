#Error Handling
'''
Error detected during execution are called exceptions
Exception will terminate a program
'''


#Error Type
'''
1. SyntaxError: Incorrect syntax
ex: print(Hello World)

2. NameError: Variable not defined
ex:
Name = 'Anna'
print(age)

3. IndexError: Out-of-range index
ex:
Student = [1,2]
print(Student[2])

4. TypeError: Incorrect type of argument
ex: print(len(6))

5. ValueError: Inappropriate value
ex: Hi = int("Hello")
'''

#Exceptions Handling
'''
1. Try-Except Statement: try blocks test a block of code for errors, when there is an error, run the except block
format: 
try:
    statement
except ErrorType:
    statement

!!!never leaves the except by itself, always except something:

2. Finally statement: finally statement let you run the code regardless of the result of try except blocks
format:
finally:
    statement

3. Else: Execute the code only when no error occurs
format:
else:
    statement

4. Raise: works like try-except block
format:
raise ErrorType(Description)

!!!Always try-except/raise when try to open, write or read a file, connect to database and etc.
'''
