x = lambda a: a + 10
print(x(5))

y = lambda a, b, c: a+b+c
print(y(5, 6, 2))

def multiplier(n)
  return lambda a: a * n
  
z = multiplier(2)
print(z(11))


'''Explanation
the first function is x, it takes a as argument and return the value a+10
print(x(5)), 5 is the a in lambda function

the second function is y, it takes a, b, c as arguments and return their sum

lastly, z = multiplier(2), 2 is the n
line 11, print(z(11)), 11 is a
'''
