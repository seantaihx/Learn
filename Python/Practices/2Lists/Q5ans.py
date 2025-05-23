'''
Insert Sorted 
Ask the user for a sorted list of numbers.
Then ask for one new number to insert.
Use .insert() to put it in the correct position to keep the list sorted.
'''

list = input("Enter a sorted number order: ")
list = list.split(' ')
new = input("Enter a new number: ")

for i in range(len(list)):
    if int(list[i]) < int(new):
        continue
    else:
        list.insert(i, new)
        break

print(list)


'''Explanation
get input, split it into a list, and get a new number to insert
write a for loop to loop through the list,
if the element is smaller than the number, since we're in order
we pass the element, until we reach the number same or greater than it
then we insert the number at the current index, move the bigger number to the next index
'''


'''SAMPLE OUTPUT
@seantaihx ➜ .../Practice/Python/Practices/2Lists (main) $ python Q5ans.py

Enter a sorted number order: 1 2 3 4 6 8 10
Enter a new number: 9
['1', '2', '3', '4', '6', '8', '9', '10']

@seantaihx ➜ .../Practice/Python/Practices/2Lists (main) $ 
'''