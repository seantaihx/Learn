'''
class ResetOnIter:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return ________  # return a new iterator object each time

# Use case
obj = ResetOnIter([10, 20])
for i in obj:
    print(i)
for j in obj:
    print(j)

Complete __iter__ so both loops print 10, 20. (Hint: You must return a new iterator each time.)
'''

class ResetOnIter:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return iter(self.data)  # return a new iterator object each time

# Use case
obj = ResetOnIter([10, 20])
for i in obj:
    print(i)
for j in obj:
    print(j)


'''SAMPLE OUTPUT
@seantaihx ➜ .../Practice/Python/Practices/8Iterators (main) $ python Q4ans.py
10
20
10
20
@seantaihx ➜ .../Practice/Python/Practices/8Iterators (main) $ 
'''