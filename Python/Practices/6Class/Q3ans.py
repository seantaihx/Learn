'''
Override the __str__() method in the Book class so that:
print(book)
prints the same string as describe().
'''

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        print(f"Title: {self.title}, Author: {self.author}")

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}"

book = Book('1984', 'George Orwell')
print(book)  # This will use __str__()
