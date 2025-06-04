'''
Write a function that returns a random element from a given list.
'''

import random as rd

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(len(list)):
    print(list[rd.randint(0, len(list)-1)])


'''SAMPLE OUTPUT
@seantaihx ➜ .../Python/Practices/10Module/2Random (main) $ python Q2ans.py
1
8
5
5
2
6
4
3
10
9
@seantaihx ➜ .../Python/Practices/10Module/2Random (main) $ 
'''