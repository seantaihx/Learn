'''
Add a method update_title(new_title) that changes the book’s title.
	•	Show before and after using describe().
'''

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        print(f"Title: {self.title}, Author: {self.author}")

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}"

    def update_title(self, new_title):
        self.title = new_title

book = Book(1984, 'George')
book.describe()
book.update_title('Sean')
book.describe()


'''SAMPLE OUTPUT
@seantaihx ➜ .../Practice/Python/Practices/6Class (main) $ python Q4ans.py
Title: 1984, Author: George
Title: Sean, Author: George
@seantaihx ➜ .../Practice/Python/Practices/6Class (main) $ 
'''

