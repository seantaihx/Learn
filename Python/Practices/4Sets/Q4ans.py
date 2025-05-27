'''
Given a list with duplicates:
data = [1, 2, 2, 3, 4, 4, 5]
	•	Convert it to a set to remove duplicates.
	•	Convert it back to a list.
	•	Print both the new list and its length.
'''

data = [1,2,2,3,4,4,5]
print(f"list: {data}, length: {len(data)}")

data = set(data)
data = list(data)
print(f"new list: {data}, new length: {len(data)}")
