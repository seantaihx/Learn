'''
Create a class MathHelper with a @staticmethod called square(n) that returns the square of n.
	•	Call it without creating an object.
'''

class MathHelper:
  def __init__(self, num):
    self.num = num
  @staticmethod
  def square(n):
    return n**2

math = MathHelper(4)
print(math.square(3))
