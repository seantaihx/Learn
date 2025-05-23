'''
Basic Calculator (Arithmetic & If-Else)
Ask the user to input two numbers and an operator (+, -, *, /) and print the result.
'''
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
operator = input("Enter an operator: ")

if operator == '+':
    print(f"{num1} {operator} {num2} = {num1+num2}")
elif operator == '-':
    print(f'{num1} {operator} {num2} = {num1-num2}')
elif operator == '*':
    print(f'{num1} {operator} {num2} = {num1*num2}')
elif operator == '/':
    print(f'{num1} {operator} {num2} = {num1/num2}')
else:
    print("Invalid operator")