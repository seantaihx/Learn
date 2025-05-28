'''
Create a function to_int(s) that converts a string to an integer.
	•	Use try-except to catch ValueError.
	•	If it fails, return "Not a valid integer".
'''

def to_int(s):
  try:
    return int(s)
  except ValueError:
    return "Not a valid integer"

def main():
  print(to_int('3'))
  print(to_int('s'))

if __name__ = '__main__':
  main()
