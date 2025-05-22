mylist = input("Enter multiple values separated by space: ")

mylist = mylist.split(' ')
print(mylist)

ans = input("Do you want to add anything (y/n): ")
if ans == 'y':
    ans = int(input("How many of them: "))
    new = input("What: ")
    if ans != 1:
        sep = input("What did you use as separator: ")
        new = new.split(sep, ans)
        mylist.extend(new)
        print(mylist)
    else:
        mylist.append(new)
        print(mylist)
        
ans = input("Do you want to remove anything (y/n): ")
if ans == 'y':
    ans = input("Is it a position or a value or all (p/v/a): ")
    if ans == 'p':
        pos = input("What position do you want to remove (can have multiple separated by space): ")
        pos = pos.split(' ')
        for i in pos:
            i = int(i)
        for i in range(len(mylist)-1, -1, -1):
            if i in pos:
                mylist.pop(i)
        print(mylist)

    elif ans == 'v':
        value = input("What value do you want to remove (can have multiple values separated by space): ")
        value = value.split(' ')

        for i in range(len(mylist)-1, -1, -1):
            if mylist[i] in value:
                mylist.remove(mylist[i])
        print(mylist)

    elif ans == 'a':
        mylist.clear()
        print(mylist)
        
'''Explanation
After the user enter the values, we split the strings into list with space as separator

if user wants to add more than 1 values, we split it again with separator and the maxsplit given by user
notice that different method is used if the user want to add more than 1 values
i just want to show append is for one value while extend is for iterable

If user wants to remove a position, we split their answer again into list and turn the position into int
(because input gets string but position is a number)
notice i use a backward for loop to iterate from the last to the first,
this is because if user wants to pop 2 position, the original list for example is [0, 1, 2]
The user wants to pop 0 and 2 position, when 0 is popped, the position of 2 becomes 1, therefore 2 will not be popped
so iterate it backward can solve the problem

if user wants to remove a value, no need to change the type since both our list and the input's values are string
now i use a different way rather than
for i in mylist:
    if i in value:
        mylist.remove(i)
both ways are acceptable

lastly if user wants to clear the list, just use clear() method.
'''



'''SAMPLE OUTPUT
@seantaihx ➜ .../Practice/Python/Guide/7String (main) $ /home/codespace/.python/current/bin/python /workspaces/Practice/Python/Guide/8Collections/8.1List_Practice.py

Enter multiple values separated by space: 0 1 2 3 4 5 6 7 8 9 10
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

Do you want to add anything (y/n): y
How many of them: 2   
What: 11 12
What did you use as separator:  
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

Do you want to remove anything (y/n): y
Is it a position or a value or all (p/v/a): p
What position do you want to remove (can have multiple separated by space): 2 5 7 9 10 12
['0', '1', '3', '4', '6', '8', '11']

@seantaihx ➜ .../Practice/Python/Guide/7String (main) $ 
'''

'''SAMPLE OUTPUT
@seantaihx ➜ .../Practice/Python/Guide/7String (main) $ /home/codespace/.python/current/bin/python /workspaces/Practice/Python/Guide/8Collections/8.1List_Practice.py

Enter multiple values separated by space: 0 1 2 3 4 5 6
['0', '1', '2', '3', '4', '5', '6']

Do you want to add anything (y/n): n
Do you want to remove anything (y/n): y
Is it a position or a value or all (p/v/a): v
What value do you want to remove (can have multiple values separated by space): 3 4 5 6
['0', '1', '2']

@seantaihx ➜ .../Practice/Python/Guide/7String (main) $ 
'''

'''SAMPLE OUTPUT
@seantaihx ➜ .../Practice/Python/Guide/7String (main) $ /home/codespace/.python/current/bin/python /workspaces/Practice/Python/Guide/8Collections/8.1List_Practice.py

Enter multiple values separated by space: 0 1 2 3 4 5 6
['0', '1', '2', '3', '4', '5', '6']
Do you want to add anything (y/n): n
Do you want to remove anything (y/n): y
Is it a position or a value or all (p/v/a): a
[]

@seantaihx ➜ .../Practice/Python/Guide/7String (main) $ 
'''