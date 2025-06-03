'''
You are building an access control system for a game.
    1.    Ask the user for their age.
    2.    Ask the user to choose an access level:
    •    1 = Teen Mode (age 13-17)
    •    2 = Adult Mode (18+)
    •    3 = Exit
    3.    Use match-case to process the selected mode.
    4.    Use if-else to check:
    •    If the user's age meets the requirement for that mode.
    •    If not, deny access.
    5.    Use isinstance() to verify the age is a number (you may need try-except if you want advanced validation).
    6.    Print the result and type of the output.
'''

#Get user input and change to int type
age = int(input("What's your age: "))
#Print the menu to the user
print("Access Level: \n  1 = Teen Mode (age 13-17) \n  2 = Adult Mode (18+) \n  3: Exit")
level = input("Enter level: ")

#Check if age is int type
check = isinstance(age, int)

#If isinstance return True, match the cases
if check:
    match level:
        case '1':
            #Only between 13 and 17 can access to this
            if age >= 13 and age <= 17:
                print("Access granted")
            else:
                print("Access deny")
        case '2':
            #Only older than 18 can access
            if age >= 18:
                print("Access granted")
            else:
                print("Access deny")
        case '3':
            print("Bye")

'''SAMPLE OUTPUT
@seantaihx ➜ .../Practice/Python/Practices/0Loops (main) $ python Q8ans.py
What's your age: 20
Access Level: 
  1 = Teen Mode (age 13-17) 
  2 = Adult Mode (18+) 
  3: Exit
Enter level: 1
Access deny
@seantaihx ➜ .../Practice/Python/Practices/0Loops (main) $ 
'''