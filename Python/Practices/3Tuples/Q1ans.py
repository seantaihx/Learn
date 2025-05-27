'''
Create a tuple containing three elements: an integer, a string, and a list.
	•	Append a new item to the list inside the tuple.
	•	Print the result
 '''

mytuple = (2, 'd', ['1', '2', '3', '4'])
mytuple[2].append('5')
print(mytuple)


'''Explanation
Tuple is immutable, so we cant directly change the tuple's element
But we can change the mutable element inside tuple
'''


'''SAMPLE OUTPUT
(2, 'd', ['1', '2', '3', '4', '5'])
'''
