'''
In the Book class, add a method describe() that prints:
"Title: [title], Author: [author]"
	•	Call this method using your object.
'''

class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author
  def describe(self):
    print(f"Title: [{self.title}], Author: [{self.author}]")

book = Book('1984', 'George Orwell')
book.describe()


'''SAMPLE OUTPUT
@seantaihx ➜ .../Practice/Python/Practices/6Class (main) $ python Q2ans.py
Title: [1984], Author: [George Orwell]
@seantaihx ➜ .../Practice/Python/Practices/6Class (main) $ 
'''
