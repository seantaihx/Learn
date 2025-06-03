'''
Add a class variable called count to track how many Book objects have been created.
	•	Each time a new book is created, increase count by 1.
	•	Print Book.count after making 3 books.
'''

class Book:
    count = 0  # Class variable

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.count += 1  # Increase count on each new object

    def describe(self):
        print(f"Title: {self.title}, Author: {self.author}")

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}"

    def update_title(self, new_title):
        self.title = new_title

book1 = Book('1984', 'George')
book2 = Book('Sean', "Sean")
book3 = Book('2112', 'Future')

print(Book.count)


'''SAMPLE OUTPUT
@seantaihx ➜ .../Practice/Python/Practices/6Class (main) $ python Q5ans.py
3
@seantaihx ➜ .../Practice/Python/Practices/6Class (main) $ 
'''