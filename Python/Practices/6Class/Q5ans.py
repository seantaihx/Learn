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
