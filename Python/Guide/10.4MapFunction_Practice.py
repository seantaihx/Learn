def mapfunc(a, b):
  return (a+b)
x = map(mapfunc, ('apple', 'banana', 'cherry'), ('1', '2', '3'))

print(list(x))

'''Explanation
we define function mapfunc, then using map function to apply the function to every element in both tuples
'''
