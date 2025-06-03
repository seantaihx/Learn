'''
Find That Word
Ask the user to enter a sentence and a keyword.
Print the position of the keyword in the sentence.
'''

print('\n')
#Get user input
sentence = input("Enter a sentence: ")
keyword = input("Enter a word you want to find: ")

#Find the position of a keyword
position = sentence.find(keyword)
print("Position: {}".format(position))
#Return -1 if not found, so this is when it's found keep looping
while position != -1:
    #Find the position start from the previous found position+1 to the end of the sentence
    position = sentence.find(keyword, position+1, len(sentence))
    if position != -1:
        print("Position: {}".format(position))
print('\n')



'''Explanation
get the input from the user 
find the keyword first to have a starting value for position
if didnt find first, there's no value in position and while loop never starts

find method returns -1 when value is not found, so position != -1 means while it is found
-1 is not found, != -1 is not not found => found

we reset the position by starting the search at the current position +1
since position is the position of the first character of the keyword,
if not position+1, we keep finding the keyword at current position (The first character's position)
so the keyword is keep founding at same position, resulting in endless loop

Notice the ending position is len(sentence) not len(sentence)-1,
this is because the ending position is not included in the find method, to include last character
we use len(sentence) as ending position
or we can just find(keyword, position + 1), just omit the end value entirely

if the position is found (!= -1), print the position
'''



'''SAMPLE OUTPUT
@seantaihx ➜ .../Practice/Python/Practices/1Strings (main) $ python Q4ans.py

Enter a sentence: Hi Hi Hi My name is Sean Hi
Enter a word you want to find: Hi
Position: 0
Position: 3
Position: 6
Position: 25

@seantaihx ➜ .../Practice/Python/Practices/1Strings (main) $ 
'''