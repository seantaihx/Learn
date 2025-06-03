'''
Add to List
Ask the user to enter 5 numbers one by one.
Use .append() to store them into a list.
Print the final list.
'''

#Create an empty list
list = []

#Enter 5 numbers
for i in range(5):
    num = int(input("Enter number: "))
    #Add them to the end of the list
    list.append(num)
print(list)


'''Explanation
create an empty list first
use a for loop to iterate 5 times, and for each time, get an input and append to list
'''

'''SAMPLE OUTPUT
@seantaihx ➜ /workspaces/Practice (main) $ cd Python/Practices/2Lists
@seantaihx ➜ .../Practice/Python/Practices/2Lists (main) $ python Q1ans.py

Enter number: 1
Enter number: 2
Enter number: 3
Enter number: 5
Enter number: 6
[1, 2, 3, 5, 6]

@seantaihx ➜ .../Practice/Python/Practices/2Lists (main) $ 
'''