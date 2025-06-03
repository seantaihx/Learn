'''
class FibUpTo:
    def __init__(self, max_value):
        self.max = max_value
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.max:
            raise StopIteration
        val = self.a
        self.a, self.b = ________
        return val

# Output: 0 1 1 2 3 5 8 13 21
for num in FibUpTo(21):
    print(num)

Complete the missing line to make the Fibonacci logic correct.
'''

class FibUpTo:
    def __init__(self, max_value):
        self.max = max_value
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.max:
            raise StopIteration
        val = self.a
        self.a, self.b = self.b, self.a + self.b  # Fibonacci logic
        return val

# Output: 0 1 1 2 3 5 8 13 21
for num in FibUpTo(21):
    print(num)