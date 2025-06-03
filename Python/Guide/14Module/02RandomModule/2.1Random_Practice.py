import random as rd

while True:
    ans = input("Enter q to quit other words to continue: ")
    if ans == 'q':
        break

    print("Roll 2 dice, win if two dice have consecutive value or equal value, otherwise lose")
    r1 = rd.randint(1,6)
    r2 = rd.randint(1,6)
    print("You rolled {} {}".format(r1, r2))

    if abs(r2-r1) == 1 or (r1 == r2):
        print("You win")

    else:
        print("You lose")
    print('\n')

'''Explanation
In the loop, if user never enters q, it's an endless loop
we store a random value between 1-6 in variable r1 and r2

if two values is the same or their subtraction is 1
print You win, else print lose
'''


'''SAMPLE OUTPUT
@seantaihx ➜ /workspaces/Practice (main) $ cd Python/Guide/Random_Module
@seantaihx ➜ .../Practice/Python/Guide/Random_Module (main) $ python .1Random_Practice.py

Enter q to quit other words to continue: 3
Roll 2 dice, win if two dice have consecutive value or equal value, otherwise lose
You rolled 3 1
You lose

Enter q to quit other words to continue: 3
Roll 2 dice, win if two dice have consecutive value or equal value, otherwise lose
You rolled 3 2
You win

Enter q to quit other words to continue: 3
Roll 2 dice, win if two dice have consecutive value or equal value, otherwise lose
You rolled 1 6
You lose

Enter q to quit other words to continue: 2
Roll 2 dice, win if two dice have consecutive value or equal value, otherwise lose
You rolled 4 2
You lose

Enter q to quit other words to continue: 2
Roll 2 dice, win if two dice have consecutive value or equal value, otherwise lose
You rolled 1 4
You lose

Enter q to quit other words to continue: 3
Roll 2 dice, win if two dice have consecutive value or equal value, otherwise lose
You rolled 2 3
You win

Enter q to quit other words to continue: 1
Roll 2 dice, win if two dice have consecutive value or equal value, otherwise lose
You rolled 1 2
You win
Enter q to quit other words to continue: q

@seantaihx ➜ .../Practice/Python/Guide/Random_Module (main) $ 
'''