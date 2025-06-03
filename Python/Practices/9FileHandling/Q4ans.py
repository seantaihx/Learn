'''
Write a function count_words(filename) that returns the number of words in the given text file.
'''

def count_words(filename):
    with open(filename, 'rt') as f:
        text = f.read()
        words = text.split()
        return len(words)


print("Word count:", count_words('Q4ans.txt'))

'''SAMPLE OUTPUT
@seantaihx ➜ .../Practice/Python/Practices/9FileHandling (main) $ python Q4ans.py
Word count: 5
@seantaihx ➜ .../Practice/Python/Practices/9FileHandling (main) $ 
'''