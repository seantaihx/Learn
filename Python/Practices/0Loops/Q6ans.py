'''
Simple Menu Using match-case (Python 3.10+)
Print a menu:
1. Say Hello
2. Say Goodbye
3. Exit
Ask user to enter a choice. Use match to perform the action.
'''

print("Menu:")
print("1. Say Hello\n2. Say Goodbye\n3. Exit\n")

while True:
    choice = input('Enter the options (1/2/3): ')

    match choice:
        case '1':
            print("Hello")
        case '2':
            print("Bye")
        case '3':
            break
print('\n')

'''SAMPLE OUTPUT
@seantaihx ➜ /workspaces/Practice (main) $ /home/codespace/.python/current/bin/python /workspaces/Practice/Python/Practices/Q6ans.py
Menu:
1. Say Hello
2. Say Goodbye
3. Exit

Enter the options (1/2/3): 1
Hello
Enter the options (1/2/3): 2
Bye
Enter the options (1/2/3): 3

@seantaihx ➜ /workspaces/Practice (main) $ 
'''