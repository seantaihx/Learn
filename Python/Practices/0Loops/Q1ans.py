'''
Basic Calculator (Arithmetic & If-Else)
Ask the user to input two numbers and an operator (+, -, *, /) and print the result.
'''


#Get user's input
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
operator = input("Enter an operator: ")

#matching the operators
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





'''Explanation
we see which operator the user input, 
and use an if-else statement to match the operator to do the respective calculation
'''





'''SAMPLE OUTPUT
@seantaihx ➜ .../Practice/Python/Practices/0Loops (main) $ python Q1ans.py
Enter number 1: 4
Enter number 2: 7
Enter an operator: *
4.0 * 7.0 = 28.0
@seantaihx ➜ .../Practice/Python/Practices/0Loops (main) $ 
'''