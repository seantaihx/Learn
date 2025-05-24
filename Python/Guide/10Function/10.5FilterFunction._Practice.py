age = [5, 12, 17, 18, 24, 32]
def func(x):
  if x < 18:
    return False
  return True


adults = filter(func, age)
for i in adults:
  print(i)


'''Explanation
we define func function, return False if smaller than 18 and return True when if not
apply the filter function to every elements in the list, 
those which returns True is stored
'''
