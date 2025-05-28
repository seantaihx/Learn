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
