'''
Max of Three Numbers (Logical + If-Else)
ask for three numbers and print the largest one using if and logical operators (and, or).
'''

a = int(input('Enter number: '))
b = int(input('Enter number: '))
c = int(input('Enter number: '))
largest = a

if largest < b:
    largest = b
if largest < c:
    largest = c

print(f"The largest number is {largest}.")