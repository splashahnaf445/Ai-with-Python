#PYTHON OOP PROBLEM-1
# You're building a simple system to manage a small library. Implement two classes:
# Book
# ● Attributes: title, author, isbn, and is_checked_out (defaults to False)
# ● Method checkout(): marks the book as checked out. If it's already checked out, print a
# message saying so instead.
# ● Method return_book(): marks the book as available again.
# ● Method __str__(): returns a readable string like "1984 by George Orwell is
# (Available)" or "...(Checked Out)".

class Book:
    def __init__(self,title,author,isbn,is_checked_out=False):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.is_checked_out=is_checked_out
    def checkout(self):
        if self.is_checked_out:
            print('The book is already checked out')
        else:
            self.is_checked_out=True
    def return_book(self):
        self.is_checked_out=False
    def __str__(self):         # __str__(self) : the __str__ method function defines what print() displays when print(object) is called
        status='Checked out' if self.is_checked_out else 'Available'
        return f"{self.title} by {self.author} is {status}"
    
book1 = Book('The 80/20 rule','Richard Coch',2004,False)
book2 = Book('Atomic habits','Unknown',1996,True)
book3 = Book('Animal Farm','Goerge Orwell',1984,False)


print(book1)
print(book2)
print(book3)

# Library
# ● Attribute: books — a list that holds Book objects (starts empty)
# ● Method add_book(book): adds a Book to the library.
# ● Method find_book(title): searches by title (case-insensitive) and returns the
# matching Book, or None if not found.
# ● Method checkout_book(title): finds the book by title and checks it out (handle the
# case where it doesn't exist).
# ● Method list_available_books(): prints all books currently available

class Library:
    def __init__(self):
        self.books=[]
    def add_book(self,Book):
        self.books.append(Book)
    def find_book(self,title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None
    def checkout_book(self,title):
        book = self.find_book(title)
        if book is None:
            print('Book not found')
        else:
            book.checkout()
    def list_available_books(self):
        print("Available books : ")
        for bk in self.books:
            if not bk.is_checked_out:
                print(bk)

library = Library()
library.add_book(Book("1984", "George Orwell", "001"))
library.add_book(Book("Brave New World", "Aldous Huxley", "002"))
library.add_book(Book("Fahrenheit 451", "Ray Bradbury", "003"))
library.checkout_book("1984")
library.checkout_book("1984")
library.checkout_book("Aquaculture")
library.list_available_books()


