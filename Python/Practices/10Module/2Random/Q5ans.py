'''
Write a function that generates a secure random 12-character password using:
	•	Letters (uppercase + lowercase)
	•	Digits
	•	Special characters (!@#$%^&*())
'''

import random as rd
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = ''.join(rd.choices(chars, k=length))
    return password

print("Generated password:", generate_password())



'''SAMPLE OUTPUT
@seantaihx ➜ .../Python/Practices/10Module/2Random (main) $ python Q5ans.py
Generated password: Czh&dSzP!*R@
@seantaihx ➜ .../Python/Practices/10Module/2Random (main) $ 
'''