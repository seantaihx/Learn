'''
Create a program that opens a file named Q1ans.txt and prints its contents.
'''


with open('Q1ans.txt', 'x') as f:
    f.write('English: \n')
    f.write('Hi, my name is Sean. \n\n')
    f.write('German: \n')
    f.write('Hi, ich bin Sean.\n')

with open('Q1ans.txt', 'rt') as f:
    print(f.read())


'''SAMPLE OUTPUT
@seantaihx ➜ .../Practice/Python/Practices/9FileHandling (main) $ python Q1.py
English: 
Hi, my name is Sean. 

German: 
Hi, ich bin Sean.

@seantaihx ➜ .../Practice/Python/Practices/9FileHandling (main) $ 
'''