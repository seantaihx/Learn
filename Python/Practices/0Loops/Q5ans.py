'''
Simple Login (Comparison + Logical)
Store a correct username and password.
Ask the user to input both.
If both match, print “Login successful”, else “Try again”.
'''

CUsername = input("What is your username: ")
CPassword = input("What is your password: ")

while True:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == CUsername and password == CPassword:
        print("Login successful")
        break
    else:
        print("Try again")
        continue
