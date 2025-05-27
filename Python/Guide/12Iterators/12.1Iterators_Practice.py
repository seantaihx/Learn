# Custom iterator that counts from a start number to an end number

class CountIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        print("Calling __iter__")
        return self  # The iterator object returns itself

    def __next__(self):
        print(f"Calling __next__: current = {self.current}")
        if self.current > self.end:
            print("Reached the end, raising StopIteration")
            raise StopIteration
        else:
            number = self.current
            self.current += 1
            return number

# Practice: Use the custom iterator in a for loop
print("=== For Loop with Iterator ===")
for num in CountIterator(1, 3):
    print(f"Got number: {num}")

print("\n=== Manual Iteration ===")
# Manual iteration using next() function
counter = CountIterator(4, 6)
iterator = iter(counter)  # Calls __iter__

while True:
    try:
        value = next(iterator)  # Calls __next__
        print(f"Manually got: {value}")
    except StopIteration:
        print("StopIteration caught, ending loop")
        break
