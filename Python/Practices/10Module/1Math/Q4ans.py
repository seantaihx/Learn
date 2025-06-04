'''
Write a function that returns all cube roots of a given complex number using De Moivre's Theorem and cmath.
'''

import cmath as c
import math as m

def cube_roots(z):
    roots = []
    r, theta = c.polar(z)
    for k in range(3):
        root_r = r**(1/3)
        root_theta = (theta + 2 * m.pi * k) / 3
        root = c.rect(root_r, root_theta)
        roots.append(root)
    return roots

z = complex(1, 1)
roots = cube_roots(z)
for i, root in enumerate(roots):
    print(f"Root {i+1}: {root}")


'''SAMPLE OUTPUT
@seantaihx ➜ .../Python/Practices/10Module/1Math (main) $ python Q4ans.py
Root 1: (1.0842150814913512+0.2905145555072514j)
Root 2: (-0.7937005259840997+0.7937005259840998j)
Root 3: (-0.2905145555072513-1.0842150814913512j)
@seantaihx ➜ .../Python/Practices/10Module/1Math (main) $ 
'''