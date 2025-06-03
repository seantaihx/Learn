'''
Count Occurrences
Ask the user to enter a sentence.
Convert it to a list of words using .split().
Ask for a word and count how many times it appears.
'''

#Get user input
inp = input("Enter a sentence: ")
#Split it into a list
list = inp.split()
#Enter a word user want to find
word = input("Enter a word you want to find: ")
#Count the word appears how many time
num = list.count(word)

print("{} appears {} times".format(word, num))


'''Explanation
get input and split them into a list (including space)
if we split "1 3" using split(), the list is ['1', ' ', '3'] but if use split(' '), the list is ['1', '3']
get input the word to find, count the word
print the num
'''


'''SAMPLE OUTPUT
@seantaihx ➜ .../Practice/Python/Practices/2Lists (main) $ python Q3ans.py

Enter a sentence: sean tai hi hi hi
Enter a word you want to find: hi
hi appears 3 times

@seantaihx ➜ .../Practice/Python/Practices/2Lists (main) $ 
'''