'''
Create a class Book with attributes title and author.
	•	Write a constructor (__init__) to initialize them.
	•	Create one book object and print its title.
'''

class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author

book = Book('1984', 'George Orwell')
print(book.title)
