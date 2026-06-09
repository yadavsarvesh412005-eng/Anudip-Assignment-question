#Create a class that returns a custom string when printed (__str__)
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title}, Author: {self.author}"

b = Book("Python", "John")

print(b)