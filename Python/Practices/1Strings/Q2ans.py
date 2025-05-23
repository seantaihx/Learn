'''
Strip It Clean
Ask the user to enter a word with spaces before and after.
Print the word with spaces removed.
'''

print('\n')
word = input("Enter a word with space before and after a word: ")
word = word.strip()
print("Now it has no space before and after the word, {}".format(word))
print('\n')


'''Explanation
Get input
strip it
print it
'''

'''SAMPLE OUTPUT
@seantaihx ➜ /workspaces/Practice/Python/Practices (main) $ cd 1Strings
@seantaihx ➜ .../Practice/Python/Practices/1Strings (main) $ python Q2ans.py

Enter a word with space before and after a word:  Hi  
Now it has no space before and after the word, Hi

@seantaihx ➜ .../Practice/Python/Practices/1Strings (main) $ 
'''