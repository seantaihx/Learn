'''
Write code to convert a complex number into polar coordinates (r, θ) using cmath.
'''

import cmath as c

a = complex(input('Enter a complex number: '))
b = c.polar(a)
print(f'The respective polar coordinate of {a} is {b}.')

'''SAMPLE OUTPUT
@seantaihx ➜ .../Python/Practices/10Module/1Math (main) $ python Q3ans.py
Enter a complex number: 2+3j
The respective polar coordinate of (2+3j) is (3.605551275463989, 0.982793723247329).
@seantaihx ➜ .../Python/Practices/10Module/1Math (main) $ 
'''