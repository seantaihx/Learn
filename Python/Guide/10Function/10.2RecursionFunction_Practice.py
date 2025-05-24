def gcf(a, b):
  if (b == 0):
    return abs(a)
  else:
    return gcf(b, a%b)

def main():
  a = int(input("Enter number 1: "))
  b = int(input("Enter number 2: "))
  g = gcf(a, b)
  print("The gcf of {} and {} is {}".format(a, b, g))


if __name__ == '__main__':
  main()
