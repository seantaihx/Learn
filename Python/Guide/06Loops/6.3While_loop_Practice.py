ans = input("Do you want a while loop with counter to stop or a break to stop (c/b): ")

if ans == 'c':
    number = int(input("Enter a number: "))
    counter = int(input("Enter the counter: "))
    while number > 0:
        print(number)
        number -= counter

elif ans == 'b':
    while True:
        a = input('Enter q to quit or other thing to continue: ')
        if a == 'q':
            break
        print('Hi')

else:
    print("?")

'''Explanation
We get the input from user to see if they wanna try break or counter to stop a while loop

if they choose counter, we prompt the user to input the number, and counter
since we treat them as a number (number -= counter) we change their type into int
so now it will keep iterating until the number is smaller than 0 (not equal to)

if they choose break, then while True means keep iterating and never stop unless break statement is used
we make a condition, when the user input q, we break the loop, if not q, print Hi
'''



'''SAMPLE OUTPUT
@seantaihx ➜ .../Practice/Python/Guide/6Loops (main) $ python 6.3While_loop_Practice.py
Do you want a while loop with counter to stop or a break to stop (c/b): c
Enter a number: 5
Enter the counter: 2
5
3
1

@seantaihx ➜ .../Practice/Python/Guide/6Loops (main) $ python 6.3While_loop_Practice.py
Do you want a while loop with counter to stop or a break to stop (c/b): b
Enter q to quit or other thing to continue: e
Hi
Enter q to quit or other thing to continue: e
Hi
Enter q to quit or other thing to continue: q

@seantaihx ➜ .../Practice/Python/Guide/6Loops (main) $ python 6.3While_loop_Practice.py
Do you want a while loop with counter to stop or a break to stop (c/b): d
?

@seantaihx ➜ .../Practice/Python/Guide/6Loops (main) $ 
'''