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
