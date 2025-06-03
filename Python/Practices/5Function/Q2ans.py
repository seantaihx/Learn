'''
Write a function get_item(lst, index) that returns the element at the given index of a list.
	•	Handle IndexError if the index is out of range.
	•	Return "Invalid index" if an error occurs.
'''

def get_item(lst, index):
  try:
    return lst[index]
  except IndexError:
    return "Invalid index"


def main():
  print(get_item([1, 2, 3], 1))   # 2
  print(get_item([1, 2, 3], 5))   # Invalid index

if __name__ == '__main__':
  main()

'''SAMPLE OUTPUT
@seantaihx ➜ .../Practice/Python/Practices/5Function (main) $ python Q2ans.py
2
Invalid index
@seantaihx ➜ .../Practice/Python/Practices/5Function (main) $ 
'''
