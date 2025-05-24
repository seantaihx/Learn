def uppercase(func):
  def wrapper():
    result = func()
    return result.upper()
  return wrapper()

@uppercase          --> this means greet = uppercase(greet())
def greet():
  return "Hello"

print(greet())


'''Explanation
define the uppercase function first, 
@uppercase means use the greet() function as the argument of uppercase function
'''
