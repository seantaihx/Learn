#Strings
'''
String: An iterable, and everything inside quotation marks is a string

It is immutable
ex: word[0] = 'H'       => Error
'''


#Indexing
'''
Index: Index is the position of something inside an iterable, it is a number

format: iterable[index]
!!!Index always start with 0, means the first character's index is 0, so the last one is length of the string -1

The last character can also has index -1, so the first character can also has index -(len)
'''


#Slicing
'''
Slicing: To get a substring inside a string using their index number

format: iterable[start_index: end_index: step(optional)]
!!!The value of start_index is included, while the end_index is not
!!!If we start the slicing at the first index, we can ignore it like [:3] 
or end at the last character too [1:], if slice whole string [:] 
or just want the even index of it [::2], or odd index [1::2]
or just print the string backward [::-1]
'''

#Length of a string
'''
Length of string: How many character are there in a string

format: len(variable/iterable)
'''


#Escape Sequence
'''
Escape Sequence: Something to use for formatting or printing values that have different meaning

\': Print '
\\: Print \
\": Print "
\n: New line
\r: Replace the word
\t: Tab (Some space)
\b: Backspace
\ooo: Octal value
\xhh: Hex value
'''


#F-string
'''
F-string: A type of formatting to directly put a value of a variable into a string

format:
1. variable = f'string...{variable}...string'
2. variable = 'string...{}...string'.format(variable)

!!!We usually just use it when printing so it's like
print(f'string...{variable}...string')
print('string... {}...string'.format(variable))
'''

#String Method
'''
String method: Something we can use to modify or can info from a string
'''

