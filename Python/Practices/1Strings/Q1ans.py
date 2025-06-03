'''
Case Converter
Ask the user to enter a word. Print it in:
	•	all lowercase
	•	all uppercase
'''

print('\n')
#Get user input
string = input("Enter some words: ")
#Make all the character lowercase
string = string.lower()
print(string)
#Make all the character uppercase
string = string.upper()
print(string)
print('\n')

'''Explanation
take an input
convert it and print lowercase
print
convert it and print uppercase
print
'''


'''SAMPLE OUTPUT
/home/codespace/.python/current/bin/python /workspaces/Practice/Python/Practices/1Strings/Q1ans.py
@seantaihx ➜ /workspaces/Practice (main) $ /home/codespace/.python/current/bin/python /workspaces/Practice/Python/Practices/1Strings/Q1ans.py

Enter some words: Sean Tai
sean tai
SEAN TAI

@seantaihx ➜ /workspaces/Practice (main) $ 
'''