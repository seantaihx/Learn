'''
Even or Odd (Modulo + If-Else)
Ask for a number. If it's even, print "Even", else print "Odd".
'''

#Get user input
num = int(input("Enter a number: "))

#See what will the remainder will be and match the respective output (even or odd)
if num%2==0:
    print('even')
else:
    print("odd")


'''Explanation
we get the input from the user

Even numbers are divisible by 2
Means the remainder when even numbers are divided by 2 is 0

Odd numbers are not divisible by 2
And the remainder when odd numbers are divided by 2 is 1

So we use if-else statement, to match and print the respective value
'''


'''SAMPLE OUTPUT
@seantaihx ➜ .../Practice/Python/Practices/0Loops (main) $ python Q2ans.py
Enter a number: 11
odd
@seantaihx ➜ .../Practice/Python/Practices/0Loops (main) $ 
'''