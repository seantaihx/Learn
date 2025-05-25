def func1(*a, b):
  for i in a:
    a += b
  return a

def func2(a, **b):
  return a+b

def func(a, b, /, c, *, d, e):
  print("a is {}".format(a))
  print("b is {}".format(b))
  print("c is {}".format(c))
  print("d is {}".format(d))
  print("e is {}".format(e))

def main():
  a = func1(1, 2, 3, 4, 5, 6, b=7)
  print(a)

  b = func2(1, b=2)
  print(b)

  func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, d=11, e=12)


main()
