'''
Write a function divide(a, b) that returns the result of a / b.
	•	Use try-except to handle division by zero.
	•	If b == 0, return "Error: cannot divide by zero".
 '''

def divide(a, b):
    try:
        a = float(a)
    except:
        return "a is not a number"
    
    try:
        b = float(b)
    except:
        return "b is not a number"
    
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: cannot divide by zero"

def main():
  print(divide(10, 2))        # 5.0
  print(divide("10", "2.5"))  # 4.0
  print(divide(10, 0))        # Error: cannot divide by zero
  print(divide("ten", 2))     # a is not a number

if __name__ == '__main__':
  main()
