a = int(input("Enter 1 number: "))
b = int(input("Enter 1 number: "))
c = int(input("Enter 1 number: "))

largest = a
if largest < b:
    largest = b
if largest < c:
    largest = c


print("Largest number is ", largest)

'''Explanation
We first assume the largest number is a, then we compare it with b to see which one is greater
if b is greater than the largest number (a for now), then b becomes the largest number, if not, then nothing

Next, we check again if the current largest is greater than c
(If b is greater than a, current largest is b, if not, current largest is a)

if c is greater than the current largest, c becomes the largest number, if not, nothing happens
'''




'''SAMPLE OUTPUT
@seantaihx ➜ .../Practice/Python/Guide/6Loops (main) $ /home/codespace/.python/current/bin/python /workspaces/Practice/Python/Guide/5Selection/5.2If-Else_Practice.py
Enter 1 number: 34
Enter 1 number: 35
Enter 1 number: 78
Largest number is  78
@seantaihx ➜ .../Practice/Python/Guide/6Loops (main) $ /home/codespace/.python/current/bin/python /workspaces/Practice/Python/Guide/5Selection/5.2If-Else_Practice.py
Enter 1 number: 34
Enter 1 number: 65
Enter 1 number: 34
Largest number is  65
@seantaihx ➜ .../Practice/Python/Guide/6Loops (main) $ 
'''