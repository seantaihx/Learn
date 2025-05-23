'''
Count Letters
Ask the user to enter a sentence and a letter.
Count how many times that letter appears in the sentence.
'''

print('\n')
sentence = input("Enter a sentence: ")
word = input("Enter a word you want to count: ")

times = sentence.count(word)

print("{} has appeared {} times".format(word, times))
print('\n')


'''Explanation
Prompt the user to enter a sentence and a word to find
find the word
count it
print it
'''

'''SAMPLE OUTPUT
@seantaihx ➜ .../Practice/Python/Practices/1Strings (main) $ python Q3ans.py

Enter a sentence: Hi Hi Hi, Ho Ho Ho, Hi Hi Hi, yo            
Enter a word you want to count: Ho
Ho has appeared 3 times

@seantaihx ➜ .../Practice/Python/Practices/1Strings (main) $ 
'''