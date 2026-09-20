class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

           
class Member():
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

class Library:
    def __init__(self):
        self.books = []

    def checkout(self, book, member):
        if not book.is_checked_out:
            book.is_checked_out = True  
            member.borrowed_books.append(book)
        else:
            print("This book is unavailable")

    def return_book(self, book, member):
        book.is_checked_out = False
        member.borrowed_books.remove(book)


book1 = Book("Hobbit", "Tolkien")
member1 = Member("Thomas")
library = Library()

library.checkout(book1, member1)
print(book1.is_checked_out)
print(member1.borrowed_books)

library.checkout(book1, member1)   

library.return_book(book1, member1)
print(book1.is_checked_out)
print(member1.borrowed_books)        
                