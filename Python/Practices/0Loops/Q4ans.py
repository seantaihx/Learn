'''
Max of Three Numbers (Logical + If-Else)
ask for three numbers and print the largest one using if and logical operators (and, or).
'''

#Get user input and change it into integer
a = int(input('Enter number: '))
b = int(input('Enter number: '))
c = int(input('Enter number: '))

#We initialize the largest as the value of a (assume a is the largest)
largest = a

#Compare it with the other two value
if largest < b:
    largest = b
if largest < c:
    largest = c

print(f"The largest number is {largest}.")


'''Explanation
We first set the largest value as a
Why?
We can set the largest to 0 if you want, so the comparing if statement will add one more
but this cannot compare value smaller than 0
If we initialize it into -value, we dont know what exact negative value is the smallest
So we initialize it as a

Then we compare it with the other 2

It is like this,
First, largest is a
If b is greater than a, current largest is b now. If not, largest is still a
Then, we compare the current largest to c, and repeat the same step

Why not if-else but two ifs?
if-else only compare the second value when the first comparison is false
so the number set 1 2 3 will result in 2 is the largest
since 2 is bigger than 1, it wont continue comparing further
'''



'''SAMPLE OUTPUT
@seantaihx ➜ .../Practice/Python/Practices/0Loops (main) $ python Q4ans.py
Enter number: 1   
Enter number: 2
Enter number: 3
The largest number is 3.
@seantaihx ➜ .../Practice/Python/Practices/0Loops (main) $ 
'''