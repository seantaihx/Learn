'''
Create a tuple with five items.
	•	Use tuple unpacking to assign each value to a separate variable.
	•	Print the variables in reverse order using only tuple unpacking.
'''

mytuples = (1, 2, 3, 4, 5)
#first element at a, second element is b...
a, b, c, d, e = mytuples
reversed_tuple = (e, d, c, b, a)

for item in reversed_tuple:
    print(item)

'''SAMPLE OUTPUT
@seantaihx ➜ .../Practice/Python/Practices/3Tuples (main) $ python Q3ans.py
5
4
3
2
1
@seantaihx ➜ .../Practice/Python/Practices/3Tuples (main) $ 
'''