#Arithmetic Operator
'''
Arithmetic Operator: plus, minus...

adding: +
subtraction: -
multiplication: *
division: /
int division: //
modulus (remainder): %
power: **

!!!Beside + and *, every other arithmetic operators can only be used on numbers

a = a + __ can be written as a += __
Can also apply to other arithmetic operator.
'''

#Some Math Thing
'''
absolute value: abs(value)
round number to specific num: round(num, how_many_decimal(optional))
'''


#Comparison Operator
'''
Comparison Operator: Return a bool value (True/False) after comparing two or more values

greater/ greater or equal to: > >=
less/ less or equal to: < <=
equal to: ==
not equal to: !=

!!!Comparing 2 string is comparing their ASCII value.
ASCII value: Most of the character has a binary value to tell the computer what character it is.
'''



#Logical Operator
'''
Logical Operator: Return bool type

and, or, &, |

& is more 'advance' version of and
| is more 'advance' version of or

True and True = True
True and False = False
False and False = False

True or True = True
True or False = True
False or False = False
'''

#Bitwise Operator (Advance)
'''
Bitwise Operator: Works directly on the binary version of numbers

In computer, numbers are in 2bits. i.e. 11001010

&, |, ^, ~, <<, >>

AND (differ from logical operator): &
Keep the 1s if both numbers has it at specific position
ex: 
6 & 3 (0110 & 0011)
=> 2 (0010)

OR (differ from logical operator): |
Take all 1s from both numbers
ex:
6 | 3 (0110 | 0011)
=> 7 (0111)

XOR: ^
Switch the position to 1 if only one number at the respective position is 1
ex:
6 ^ 3 (0110 ^ 0011)
=> 5 (0101)

NOT: ~
Inverts all bits
ex:
~8 (1000)
=> 7 (0111)

LEFT SHIFT: <<
Shifts bits to the left (Numbers x 2)
ex:
2 << 1 (0010)
=> 4 (0100)

RIGHT SHIFT: >>
Shifts bits to the right (Numbers / 2)
ex:
2 >> 1 (0010)
=> 1 (0001)

!!!CANNOT use on strings
'''


#Other
'''
in: Check if something is inside a string or collection
not in: Check if something is not inside a string or collection
not: The opposite of bool value
'''
