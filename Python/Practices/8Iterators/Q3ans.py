'''
def even_up_to_10():
    for i in range(11):
        if ______:
            yield ______

for num in even_up_to_10():
    print(num)
    
Complete the function to only yield even numbers from 0 to 10.
'''

def even_up_to_10():
    for i in range(11):
        if i % 2 == 0:
            yield i

for num in even_up_to_10():
    print(num)

'''SAMPLE OUTPUT
@seantaihx ➜ .../Practice/Python/Practices/8Iterators (main) $ python Q3ans.py
0
2
4
6
8
10
@seantaihx ➜ .../Practice/Python/Practices/8Iterators (main) $ 
'''