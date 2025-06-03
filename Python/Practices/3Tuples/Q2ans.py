'''
Given a tuple of numbers:
numbers = (5, 3, 7, 3, 9, 3, 1)
  •	Print how many times 3 appears.
	•	Find the index of its second occurrence.
'''

numbers = (5, 3, 7, 3, 9, 3, 1)
#Count the numbers it appears how many times
c = numbers.count(3)
print(f'it appears {c} times')
#Go through the tuple
for i in range(len(numbers)):
  #If the element is 3
  if numbers[i] == 3:
    #If it appears the first time, keep on going
    if i == numbers.index(3):
      continue
    #Else print the index
    else:
      print(f'It also appears at {i}.')
      continue
  else:
    continue

#Or

'''
numbers = (5, 3, 7, 3, 9, 3, 1)
c = numbers.count(3)
print("Count:", c)
first_index = numbers.index(3)
second_index = numbers.index(3, first_index + 1)
print("Second index:", second_index)
'''



'''SAMPLE OUTPUT
@seantaihx ➜ .../Practice/Python/Practices/3Tuples (main) $ python Q2ans.py
it appears 3 times
It also appears at 3.
It also appears at 5.
@seantaihx ➜ .../Practice/Python/Practices/3Tuples (main) $ 
'''