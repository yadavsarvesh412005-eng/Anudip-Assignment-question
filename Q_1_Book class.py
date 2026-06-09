# Question 1:
#  Book class and search by author

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

def search_author(books, author):
    return [b.title for b in books if b.author == author]

b1 = Book("Python", "John")
b2 = Book("Java", "Mike")
b3 = Book("C++", "John")

print(search_author([b1, b2, b3], "John"))
