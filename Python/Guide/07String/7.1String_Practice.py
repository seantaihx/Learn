string = input("Enter a string: ")

print(f"The first character is {string[0]} while the last character is {string[len(string)-1]}.")
print("The string has {} characters".format(len(string)))

print("The first two characters of the string are {}".format(string[:2]))
print("The last two characters of the string are {}".format(string[-2:]))

print("The even index of the string (0,2,4..) is {}".format(string[::2]))


'''Explanation
After the user enter a string, we use f string to see the first character of the string and last.
(string[len(string)-1]) is string with position (len(string)-1), length of the string -1 (because index start with 1)

Then we use another type of f-string to find the length of string to see how many character it has.

After that we use slicing to find first two and last two, notice the index can be negative in python

The step is skipped by 2 using slicing too
'''

'''SAMPLE OUTPUT
@seantaihx ➜ .../Practice/Python/Guide/6Loops (main) $ cd ..
@seantaihx ➜ /workspaces/Practice/Python/Guide (main) $ cd 7String
@seantaihx ➜ .../Practice/Python/Guide/7String (main) $ python 7.1String_Practice.py

Enter a string: Sean Tai
The first character is S while the last character is i.
The string has 8 characters
The first two characters of the string are Se
The last two characters of the string are ai
The even index of the string is Sa a

@seantaihx ➜ .../Practice/Python/Guide/7String (main) $ 
'''