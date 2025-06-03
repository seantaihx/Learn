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

'''SAMPLE OUTPUT
@seantaihx ➜ /workspaces/Practice (main) $ /home/codespace/.python/current/bin/python /workspaces/Practice/Python/Practices/4Sets/Q4ans.py
list: [1, 2, 2, 3, 4, 4, 5], length: 7
new list: [1, 2, 3, 4, 5], new length: 5
@seantaihx ➜ /workspaces/Practice (main) $ 
'''