while True:
    a = input("press q to quit loop or a number: ") #If not press q, this is an endless loop
    if a == 'q':
        break                                      #Break the loop if a is q
    a = int(a)                                     #Change the type of a into int, cause range() take int

    for i in range(a):                             #i is the value of current iteration, the value start from 0 to a
        print(i, " ")                                   #print i
    print('\n')

    for i in range(0, a, 3):                    #i is th value start from 0 to a, and add 3 at a time (0, 3, 6..)
        print(i, " ")
    print('\n')

a = 100
print("Now a is 100")
while a >= 0:
    if a == 50:
        a -= 10
        continue                #Skip the iteration when a is 50
    if a == 30:
        break                   #break the loop when a is 30
    print(a)
    a -= 10
print('\n')

a = 3
print("Now a is 3")
while a>=0:
    print(a)
    a -= 1                                  #This is the counter to prevent endless loop
print('\n')

print("Now try 'in': ")
a = input("Enter a string: ")
for i in a:                         #Loop through every character of the string
    print(i)

print('\n')

for i in 'cjhfbh':                  #Loop through cjhfbh
    print(i)
print('\n')

a = [1, 2, 3]
for i in a:
    for j in a:
        print(i,j)                  #Nester for loop

'''
The nester for loop act like this:

i start with the first element which is 1
j start from 1 too
when i is 1, j iterate from 1 to 3, and when j is finish the whole iteration, i move to the next element 2
so it will be like 11, 12, 13, 21, 22, 23, 31, 32, 33
'''



'''SAMPLE OUTPUT
@seantaihx ➜ .../Practice/Python/Guide/6Loops (main) $ python 6.1Practice.py
press q to quit loop or a number: 4
0  
1  
2  
3  


0  
3  


press q to quit loop or a number: q
Now a is 100
100
90
80
70
60
40


Now a is 3
3
2
1
0


Now try 'in': 
Enter a string: Sean
S
e
a
n


c
j
h
f
b
h


1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
3 3
'''