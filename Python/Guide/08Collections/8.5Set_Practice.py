list1 = ["apple", "banana", "orange", "apple", "grape"]
list2 = ["banana", "kiwi", "apple", "melon", "banana"]

for i in range(len(list1)):
    c = list1.count(list1[i])
    if c != 1:
        if i != list1.index(list1[i]):
            continue
        print("{} appears {} time".format(list1[i], c))
    
for i in range(len(list2)):
    c = list2.count(list2[i])
    if c != 1:
        if i != list2.index(list2[i]):
            continue
        print("{} appears {} time".format(list2[i], c))


set1 = set(list1)
set2 = set(list2)

print(set1)
print(set2)

print("Both family has {}".format(set1.intersection(set2)))

print("Only family 1 want to buy {}".format(set1.difference(set2)))
      
more1 = input("Do family 1 want to add more things to buy: ")
if more1.strip().lower() == 'yes':
    what1 = input("Enter new things to buy separated by space: ")
    what1 = what1.split(' ')
    what1 = set(what1)
    set1.update(what1)

less1 = input("Do family 1 want to remove anything: ")
if less1.strip().lower() == 'yes':
    know = input("Do they know exactly if the item is inside the list: ")
    if know.strip().lower() == 'yes':
        while True:
            what1 = input("What to remove (q to quit): ")
            if what1 == 'q':
                break
            set1.remove(what1)
    if know.strip().lower() == 'no':
        while True:
            what1 = input("What to remove (q to quit): ")
            if what1 == 'q':
                break
            set1.discard(what1)



more2 = input("Do family 2 want to add more things to buy: ")
if more2.strip().lower() == 'yes':
    while True:
        what2 = input("Enter one new thing (q to stop): ")
        if what2 == 'q':
            break
        set2.add(what2)
    

less2 = input("Do family 2 want to remove anything: ")
if less2.strip().lower() == 'yes':
    know = input("Do they know exactly if the item is inside the list: ")
    if know.strip().lower() == 'yes':
        while True:
            what2 = input("What to remove (q to quit): ")
            if what2 == 'q':
                break
            set2.remove(what2)
    if know.strip().lower() == 'no':
        while True:
            what2 = input("What to remove (q to quit): ")
            if what2 == 'q':
                break
            set2.discard(what2)

print(set1)
print(set2)

f1 = input("Did family 1 buy those things: ")
if f1.strip().lower() == 'yes':
    set1.clear()

f2 = input("Did family 2 buy those things: ")
if f2.strip().lower() == 'yes':
    set2.clear()


'''Explanation
list1 and 2 is a grocery list from 2 family, we first see if there's anything repeated and print it out
turn the list into set, and print it out

we check what appears in both family and just in set1

if user wants to add
then, we get a list of food to add, turn it into set, and use update() since it is an iterable to add

if user wants to remove
then we use remove() or discard() depends on if they know exactly what was in the list
because remove() will result in error if the value is not in the set while discard wont


for family 2
every other things are the same except it uses add() instead of update()
add() is adding one at a time
'''




'''SAMPLE OUTPUT
@seantaihx ➜ .../Practice/Python/Guide/8Collections (main) $ python 8.5Set_Practice.py

apple appears 2 time
banana appears 2 time

{'orange', 'banana', 'grape', 'apple'}
{'kiwi', 'banana', 'apple', 'melon'}

Both family has {'banana', 'apple'}
Only family 1 want to buy {'orange', 'grape'}

Do family 1 want to add more things to buy: yes
Enter new things to buy separated by space: a b c d

Do family 1 want to remove anything: yes
Do they know exactly if the item is inside the list: no
What to remove (q to quit): a b e f
What to remove (q to quit): a 
What to remove (q to quit): b
What to remove (q to quit): e
What to remove (q to quit): f
What to remove (q to quit): q

Do family 2 want to add more things to buy: yes
Enter one new thing (q to stop): a
Enter one new thing (q to stop): b
Enter one new thing (q to stop): e
Enter one new thing (q to stop): f
Enter one new thing (q to stop): q

Do family 2 want to remove anything: yes
Do they know exactly if the item is inside the list: yes
What to remove (q to quit): a
What to remove (q to quit): b
What to remove (q to quit): q

{'c', 'banana', 'd', 'orange', 'grape', 'apple'}
{'banana', 'f', 'e', 'kiwi', 'apple', 'melon'}

Did family 1 buy those things: yes
Did family 2 buy those things: yes

@seantaihx ➜ .../Practice/Python/Guide/8Collections (main) $ 
'''