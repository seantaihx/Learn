#For Loop
'''
For loop: Used for iterating over a sequence

format:
1. for variable_for_index in range (number_of_iteration, step, order(backward = -1, optional)):
        statement
2. for variable_for_index in range(start_pos, end_pos, step(optional, default is 1), order(backward = -1, optional)):
        statement
3. for variable_for_index in iterable:
        statement

!!!iterable is a variable or value that can be iterated (string, list, dictionary...)
!!!range() take int number as argument
!!!If you want to iterate backward, in range(length, -step, -1) notice the step is negative
for i in range(2):                => This is same as for i in range(0,2,1)
        print(i)                        --> 0, 1



Nested for loop: A for loop inside a for loop
format:
for variable_for_index1 in ..:
    for variable_for_index2 in ..:
        statement

!!!first variable for index cannot be same as the second
'''

#While loop
'''
While loop: Iteration that keep repeating until condition returns False

format:
while condition:
    statement
    counter

!!!We need to set a counter for while loop to prevent an infinite loop (a loop that never ends) or a 
   condition to break the loop.

Or we can check if some condition is met (controlled by user), stop the loop

format:
while True:
        a = input("message")
        if a == 'something to stop':
                break
'''

#Loop Statement
'''
Loop Statement: Statement that can ONLY be used in loops

1. break statement: Terminate the loop entirely
2. continue statement: Stops the current iteration and skips to next iteration of the loop
3. pass statement: Do nothing, act as a placeholder
'''
