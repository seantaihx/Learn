'''
Simple Login (Comparison + Logical)
Store a correct username and password.
Ask the user to input both.
If both match, print “Login successful”, else “Try again”.
'''

#Get user input for the correct username and password
CUsername = input("What is your username: ")
CPassword = input("What is your password: ")

#use an infinity loop to get the user to input username and password
while True:
    username = input("Enter username: ")
    password = input("Enter password: ")
    #If it's correct
    if username == CUsername and password == CPassword:
        print("Login successful")
        break
    #If incorrect
    else:
        print("Try again")
        continue

'''SAMPLE OUTPUT
@seantaihx ➜ .../Practice/Python/Practices/0Loops (main) $ python Q5ans.py
What is your username: seantai184@gmail.com
What is your password: 123abc
Enter username: seantai184@gmail.com
Enter password: e
Try again
Enter username: 2
Enter password: d
Try again
Enter username: 123abc
Enter password: d
Try again
Enter username: seantai184@gmail.com
Enter password: 123abc
Login successful
@seantaihx ➜ .../Practice/Python/Practices/0Loops (main) $ 
'''