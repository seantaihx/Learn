'''
You have the tuple:
fruits = ('apple', 'banana', 'cherry')
	•	Use enumerate() to print each item with its position in the format:
    1: apple, 2: banana, etc. (Start count at 1)
'''

fruits = ('apple', 'banana', 'cherry')

for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")


'''SAMPLE OUTPUT
1: apple
2: banana
3: cherry
'''
