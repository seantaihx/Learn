cart = {
    "apple": 3,
    "banana": 2,
    "orange": 5
}

print(cart)

more = input("Does the user buy more things: ")
if more.strip().lower() == 'yes':
    while True:
        new = input("Enter what thing they buy or q to quit: ")
        if new == 'q':
            break
        num = int(input("Enter amount: "))
        if new in cart:
            cart.update({new: cart.get(new)+num})
        else:
            cart.update({new: num})

less = input("Does the user put back something: ")
if less.strip().lower() == 'yes':
    while True:
        what = input("What (q to quit): ")
        if what == 'q':
            break
        amount = int(input("How many: "))
        if cart.get(what)-amount == 0:
            cart.pop(what)
        else:
            cart.update({what: cart.get(what)-amount})

check = input("Do you want to check if something in the cart: ")
if check.strip().lower() == 'yes':
    while True:
        what = input("What (q to quit): ")
        if what == 'q':
            break
        elif what in cart:
            print("It is in the cart")
        else:
            print("It is not in the cart")

print(cart)

cart.clear()
print(cart)


'''Explanation
have a dictionary, if user inputs yes, see what they want to buy more
if that thing is in the dictionary, add the value, else add an item to the dictionary

see if user want to put back something
check if the amount is less than or equal to the amount in the cart
if it's equal to the amount, remove the whole item, else just decrease the value of the key

see if user want to check something is in the cart
if it's in, print, if not, print
'''



'''SAMPLE OUTPUT
@seantaihx ➜ .../Practice/Python/Guide/8Collections (main) $ python 8.7Dictionary_Practice.py

{'apple': 3, 'banana': 2, 'orange': 5}

Does the user buy more things: yes
Enter what thing they buy or q to quit: apple
Enter amount: 2
Enter what thing they buy or q to quit: a
Enter amount: 3
Enter what thing they buy or q to quit: q

Does the user put back something: yes
What (q to quit): banana
How many: 2
What (q to quit): orange
How many: 3
What (q to quit): q

Do you want to check if something in the cart: yes
What (q to quit): banana
It is not in the cart
What (q to quit): orange
It is in the cart
What (q to quit): q

{'apple': 5, 'orange': 2, 'a': 3}
{}

@seantaihx ➜ .../Practice/Python/Guide/8Collections (main) $ 
'''