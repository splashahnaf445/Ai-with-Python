# Problem 5: The Library Card (Classes)
# Create a simple class called Book that represents a book in a small library.
# Requirements:
# 1. The class should store title, author, and is_borrowed (a boolean, default False).
# 2. Add a method borrow() that sets is_borrowed to True and prints a message.
# 3. Add a method return_book() that sets is_borrowed to False and prints a message.
# class Book:
# def __init__(self, title, author):
# # your code here
# pass
# def borrow(self):
# # your code here
# pass
# def return_book(self):
# # your code here
# pass
# my_book = Book("The Old Man and the Sea", "Ernest Hemingway")
# my_book.borrow()
# my_book.return_book()

class Book:
    def __init__(self,title,author,is_borrowed=False):
        self.title=title
        self.author=author
        self.is_borrowed=is_borrowed
    def borrow(self):
        self.is_borrowed=True
        print('The book is borrowed')
    def return_book(self):
        self.is_borrowed=False
        print('The book is Available')

my_book = Book("The Old Man and the Sea", "Ernest Hemingway")
my_book.borrow()
my_book.return_book()