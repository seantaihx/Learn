word = input("Enter a string: ")
find_alphabet = input("Which alphabet are you looking for: ")
find = False
number = 0

for i in word:
    if i == find_alphabet:
        print("The alphabet is in the string.")
        find = True
        number += 1
        continue
    else:
        continue

if not find:
    print("It is not found")

print("It occurs ", number, " times.")

for i in range(0, number, 2):
    print(i)

'''Explanation
After we get the input, we iterate through the string, if the character match the one we're finding
print it's in the string, find becomes True and number add 1, then continue to next iteration,
if not match, continue the next iteration

since find is initially False, we say if not find, not False = True
so this will only occur when find is False (not True = False), print it's not found

after that we have a iteration start from 0 to the number it occurs, add 2 at a time, print i
'''

'''SAMPLE OUTPUT
@seantaihx ➜ .../Practice/Python/Guide/6Loops (main) $ python 6.2For_loop_Practice.py
Enter a string: Sean Taiii
Which alphabet are you looking for: i
The alphabet is in the string.
The alphabet is in the string.
The alphabet is in the string.
It occurs  3  times.
0
2

@seantaihx ➜ .../Practice/Python/Guide/6Loops (main) $ python 6.2For_loop_Practice.py
Enter a string: Sean Taiii
Which alphabet are you looking for: z
It is not found
It occurs  0  times.
@seantaihx ➜ .../Practice/Python/Guide/6Loops (main) $ 
'''