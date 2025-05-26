class CountToFive:
    def __init__(self):
        self.current = 1

    def __iter__(self):
        return self  # The object itself is the iterator

    def __next__(self):
        if self.current <= 5:
            number = self.current
            self.current += 1
            return number
        else:
            raise StopIteration  # Ends the loop


counter = CountToFive()

# Looping using for-loop (automatically uses __iter__ and __next__)
for number in counter:
    print(number)




'''SAMPLE OUTPUT
1
2
3
4
5
'''
