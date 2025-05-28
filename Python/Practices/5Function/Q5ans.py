'''
Write a function safe_add(a, b) that adds two values.
	•	If either a or b is not a number (int or float), catch the error and return "Invalid input".
'''

def safe_add(a, b):
  try:
    a=int(a)
    b=int(b)
    return a+b
  except ValueError:
    return "Invalid input"

print(safe_add(5, 3))        # 8.0
print(safe_add("4", "2.5"))  # 6.5
print(safe_add("hello", 2))  # Invalid input
