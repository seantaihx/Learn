'''
Shuffle a list of numbers from 1 to 10 and print the shuffled list.
'''

import random as rd

numbers = list(range(1, 11)) 
rd.shuffle(numbers)

print("Shuffled list:", numbers)


'''SAMPLE OUTPUT
@seantaihx ➜ .../Python/Practices/10Module/2Random (main) $ python Q3ans.py
Shuffled list: [4, 3, 1, 10, 9, 8, 5, 6, 7, 2]
@seantaihx ➜ .../Python/Practices/10Module/2Random (main) $ 
'''