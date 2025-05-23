'''
Palindrome Checker
Ask the user to enter a word.
Check if it reads the same forward and backward (e.g. “madam”).
'''

word = input("Enter a word: ").strip().lower()
palindrome = True

for i in range(len(word)):
    if word[i] == word[len(word)-1-i]:
        if len(word)%2==1:
            if i == len(word)-1-i:
                break
        elif len(word)%2==0:
            if i == (len(word)-1)//2: #maddam 0 1 2 3 4 5
                break
        continue
    else:
        palindrome = False
        break

if palindrome:
    print("It is a palindrome")
else:
    print("It is not a palindrome")


'''Explanation
Get an input of a word and set a bool value to true first
strip to prevent a space and lower to ignore case problem
We assume it is a palindrome first

use a for loop iterate (the number of character the word has) times
we start comparing forward from the start (i start from 0)
and backward from the last character (len(word)-1-i)
len(word)-1 is the last character, last character - i
for example first character, i=0, compare with last-0 = last
second character, i=1, compare with last-1 = lastsecond
if they're the same, continue to next loop

since we check forward and backward together, when it reach the half of the word, we checked all of the character
if the length of the word is odd number, we check if the index i is equal to len-1-i
for example madam has 5 characters, with index 0 1 2 3 4,
both i and len(madam)-1-i will reach 2 and this means it reach the middle of the word
means we checked the word completely, no need further checking, so break

if the length of the word is even number, we check if the index of i is the integer division of the len of the word
for example maddam, since i will never equal to len-1-i, len-1 of maddam is 5, 5//2 is 3
when i is 2, it means it reach the first d, comparing to the second d, and that is the last character to check
so we checked the word completely again, no need further checking, so break

else if the comparing character is not equal, we set the palindrome to false and break the loop
'''

#There is a better alternative
'''
word = input("Enter a word: ").strip().lower()

if word = word[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
'''





'''SAMPLE OUTPUT
@seantaihx ➜ .../Practice/Python/Practices/1Strings (main) $ python Q7ans.py
Enter a word: madam
It is a palindrome

@seantaihx ➜ .../Practice/Python/Practices/1Strings (main) $ python Q7ans.py
Enter a word: maddam
It is a palindrome

@seantaihx ➜ .../Practice/Python/Practices/1Strings (main) $ python Q7ans.py
Enter a word: madtam
It is not a palindrome

@seantaihx ➜ .../Practice/Python/Practices/1Strings (main) $ python Q7ans.py
Enter a word: no
It is not a palindrome

@seantaihx ➜ .../Practice/Python/Practices/1Strings (main) $ 
'''







