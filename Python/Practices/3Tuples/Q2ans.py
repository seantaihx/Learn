'''
Given a tuple of numbers:
numbers = (5, 3, 7, 3, 9, 3, 1)
  •	Print how many times 3 appears.
	•	Find the index of its second occurrence.
'''

numbers = (5, 3, 7, 3, 9, 3, 1)
c = numbers.count(3)
print(c)
for i in range(len(numbers)):
  if numbers[i] == 3:
    if i == numbers.index(3):
      continue
    else:
      print(i)
      break
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
