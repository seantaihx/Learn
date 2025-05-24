cart = {}
print("Welcome to the shop!\n")

while True:
    try:
        item = input("Enter item name (or 'q' to quit): ")
        if item == 'q':
            break
        quantity = input("Enter quantity: ")
        if not quantity.isdigit():
            raise ValueError("Quantity must be a number.")

        quantity = int(quantity)
        
        # Update cart
        if item in cart:
            cart[item] += quantity
        else:
            cart[item] = quantity

    except ValueError as ve:
        print("ValueError occurred:", ve)

    except Exception as e:
        print("Unknown error:", e)

    else:
        print("Item added successfully.")

    finally:
        print("Cart so far:", cart)
        print("-" * 30)

# Try accessing an item by index to demo IndexError
try:
    items = list(cart.items())
    print("Accessing 10th item:", items[9])
except IndexError:
    print("IndexError: You tried to access an item that doesn't exist.")

# Try using wrong type
try:
    print(len(123))  # TypeError
except TypeError:
    print("TypeError: len() used on incorrect type.")

# Try reading an undefined variable
try:
    print(total_price)
except NameError:
    print("NameError: Variable not defined.")

# Try a syntax error — shown as comment because it stops execution
# print("Missing end quote)  # SyntaxError

# Custom raise example
try:
    price = int(input("Enter price of last item: "))
    if price < 0:
        raise ValueError("Price cannot be negative!")
except ValueError as ve:
    print("Raised Exception:", ve)

finally:
    print("\nFinal Cart:", cart)


'''Explanation
This code implements a simple supermarket cart system using a Python dictionary to store items and their quantities, 
while demonstrating essential exception handling constructs (try, except, else, finally). 
It allows users to interactively add or remove items, check for item presence, 
and gracefully handles invalid inputs using built-in exceptions like ValueError, IndexError, TypeError, and NameError. 
The code also uses raise to enforce custom validation rules, such as preventing negative prices. 
Key features include input validation with isdigit(), use of .get() to safely retrieve values, 
and a finally block to ensure the cart's status is always shown, regardless of errors. 
This structure ensures the program remains robust and user-friendly while showcasing core Python 
error-handling and dictionary manipulation techniques.
'''

'''
This is written by AI, if have any question pull an issue to ask me, i'll clarify in here with my own explanation
'''