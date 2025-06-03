'''
nums = [100, 200, 300]
it = ______(nums)
print(______)
print(______)

Fill in the blanks to print the first two elements of the list using an iterator.
'''

nums = [100, 200, 300]
it = iter(nums)
print(next(it))
print(next(it))

'''SAMPLE OUTPUT
@seantaihx ➜ .../Practice/Python/Practices/8Iterators (main) $ python Q1ans.py
100
200
@seantaihx ➜ .../Practice/Python/Practices/8Iterators (main) $ 
'''