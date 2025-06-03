'''
class OneToN:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def ____________(self):  # complete this method
        if self.current > self.n:
            raise ____________
        val = self.current
        self.current += 1
        return val

it = OneToN(3)
print(next(it))
print(next(it))
print(next(it))

Fill in the blanks so that this class works like an iterator.
'''

class OneToN:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):  # complete this method
        if self.current > self.n:
            raise StopIteration
        val = self.current
        self.current += 1
        return val

it = OneToN(3)
print(next(it))
print(next(it))
print(next(it))