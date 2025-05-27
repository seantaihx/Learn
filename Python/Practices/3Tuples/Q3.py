'''
Create a tuple with five items.
	•	Use tuple unpacking to assign each value to a separate variable.
	•	Print the variables in reverse order using only tuple unpacking.
'''

mytuples = (1, 2, 3, 4, 5)
a, b, c, d, e = mytuples
reversed_tuple = (e, d, c, b, a)

for item in reversed_tuple:
    print(item)
