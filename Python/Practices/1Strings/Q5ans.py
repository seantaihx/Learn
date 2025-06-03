'''
Replace Words
Ask the user to enter a sentence and replace all “bad” words (like “dumb”) with “smart”.
'''

print('\n')
#Get the input
sentence = input("Enter a sentence with \"dumb\" inside: ")
#Replace the word 'dumb' to 'smart'
sentence = sentence.replace("dumb", "smart")

print(sentence)
print('\n')


'''Explanation
Prompt the user to enter a sentence with dumb inside
replace the word
print it
'''

'''SAMPLE OUTPUT
@seantaihx ➜ .../Practice/Python/Practices/1Strings (main) $ python Q5ans.py

Enter a sentence with "dumb" inside: You are dumb
You are smart

@seantaihx ➜ .../Practice/Python/Practices/1Strings (main) $ 
'''