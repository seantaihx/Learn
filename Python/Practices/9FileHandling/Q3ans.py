'''
Write a function read_partial(filename, num_chars) 
that reads only the first num_chars characters from the file and returns them.
'''

def read_partial(filename, num_chars):
    with open(filename, 'rt') as f:
        return f.read(num_chars)

# Example usage
num = int(input("How many characters you want to see: "))
result = read_partial('Q3ans.txt', num)
print(f"First {num} characters: {result}")


'''SAMPLE OUTPUT
@seantaihx ➜ .../Practice/Python/Practices/9FileHandling (main) $ python Q3ans.py
How many characters you want to see: 10
First 10 characters: Name: Sean
@seantaihx ➜ .../Practice/Python/Practices/9FileHandling (main) $ 
'''