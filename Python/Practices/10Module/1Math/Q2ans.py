'''
Write a function that takes a complex number and returns its phase (angle) in radians using cmath.
'''

import cmath as c

def phase(num):
    return c.phase(num)

while True:
    a = input("Enter a complex number or q to quit: ")
    if a == 'q':
        break
    a = complex(a)
    pa = phase(a)
    print(f'The phase angle of {a} is {pa}rad.')

'''SAMPLE OUTPUT
@seantaihx ➜ .../Python/Practices/10Module/1Math (main) $ python Q2ans.py
Enter a complex number or q to quit: 2+3j
The phase angle of (2+3j) is 0.982793723247329rad.
Enter a complex number or q to quit: 5+2j
The phase angle of (5+2j) is 0.3805063771123649rad.
Enter a complex number or q to quit: q
@seantaihx ➜ .../Python/Practices/10Module/1Math (main) $ 
'''