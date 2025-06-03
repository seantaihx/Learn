'''
Given two sets:
set1 = {1, 2, 3, 4}  
set2 = {3, 4, 5, 6}
	•	Print their intersection, union, and difference (set1 - set2).
'''

set1 = {1, 2, 3, 4}  
set2 = {3, 4, 5, 6}
print(set1.intersection(set2))
print(set1.union(set2))
print(set1-set2)


'''SAMPLE OUTPUT
@seantaihx ➜ .../Practice/Python/Practices/4Sets (main) $ python Q2ans.py
{3, 4}
{1, 2, 3, 4, 5, 6}
{1, 2}
@seantaihx ➜ .../Practice/Python/Practices/4Sets (main) $ 
'''