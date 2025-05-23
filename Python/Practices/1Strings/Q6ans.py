'''
Calculator
Ask the user to input an arithmetic equation
Print the result
'''

inp = input("Enter an arithmetic equation with space in between (n1 +-*/^ n2): ")

eqn = inp.split(' ')
n1 = int(eqn[0])
n2 = int(eqn[2])

if eqn[1] == '+':
    print("{} = {}".format(inp, n1+n2))
elif eqn[1] == '-':
    print("{} = {}".format(inp, n1-n2))
elif eqn[1] == '*':
    print("{} = {}".format(inp, n1*n2))
elif eqn[1] == '/':
    print("{} = {}".format(inp, n1/n2))
elif eqn[1] == '^':
    print("{} = {}".format(inp, n1**n2))
else:
    print("What")
print('\n')


'''Explanation
get input and split the input into a list with space as separator
check the second value of the list and see which operator the user enter
the first and third is the number
print the result
'''




'''SAMPLE OUTPUT
@seantaihx ➜ .../Practice/Python/Practices/1Strings (main) $ python Q6ans.py

Enter an arithmetic equation with space in between (n1 +-*/^ n2): 2 + 1
2 + 1 = 3

@seantaihx ➜ .../Practice/Python/Practices/1Strings (main) $ python Q6ans.py
Enter an arithmetic equation with space in between (n1 +-*/^ n2): 2 - 1
2 - 1 = 1

@seantaihx ➜ .../Practice/Python/Practices/1Strings (main) $ python Q6ans.py
Enter an arithmetic equation with space in between (n1 +-*/^ n2): 2 * 3
2 * 3 = 6

@seantaihx ➜ .../Practice/Python/Practices/1Strings (main) $ python Q6ans.py
Enter an arithmetic equation with space in between (n1 +-*/^ n2): 3 / 3
3 / 3 = 1.0

@seantaihx ➜ .../Practice/Python/Practices/1Strings (main) $ python Q6ans.py
Enter an arithmetic equation with space in between (n1 +-*/^ n2): 3 ^ 2
3 ^ 2 = 9

@seantaihx ➜ .../Practice/Python/Practices/1Strings (main) $ 
'''