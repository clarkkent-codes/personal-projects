class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.availability = True

class Library():
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, title):
        found = False
        for book in self.books:
            if title == book.title:
                if book.availability == True:
                    print(f"Successfully borrowed book {title}")
                    book.availability = False
                elif book.availability == False:
                    print(f"Book {title} is already borrowed")
                found = True
                break   # stop checking once you found the book

        if not found:
            print(f"Book {title} not Found!")


    def return_book(self, title):
        found = False
        for book in self.books:
            if title == book.title:
                if book.availability == False:
                    print(f"Successfully returned book {title}")
                    book.availability = True
                elif book.availability == True:
                    print(f"Book {title} was never borrowed")
                found = True
                break

        if not found:
            print(f"Book {title} not Found!")


    def list_books(self):
        for book in self.books:
            if len(self.books) < 0:
                print("There are no books")
            else:
                print(f"Title: {book.title} | Availability: {book.availability}")

book1 = Book("Sample Book1", "Sample Author1") 
book2 = Book("Sample Book2", "Sample Author2")
book3 = Book("Sample Book3", "Sample Author3")
book4 = Book("Sample Book4", "Sample Author4")
book5 = Book("Sample Book5", "Sample Author5") 
book6 = Book("Sample Book7", "Sample Author6")

library = Library()


print('\n')
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(book5)
library.add_book(book6)

library.borrow_book("Sample Book1")
print('\n')
library.borrow_book("Sample Book2")
print('\n')
library.borrow_book("Sample Book10")
print('\n')
library.return_book("Sample Book6")
print('\n')
library.return_book("Sample Book7")

library.list_books()


# book_in_library = {
#         ("Sample Book1", "Sample Author1"),
#         ("Sample Book2", "Sample Author2"),
#         ("Sample Book3", "Sample Author3"),
#         ("Sample Book4", "Sample Author4"),
#         ("Sample Book5", "Sample Author5"),
#         ("Sample Book7", "Sample Author6")
# }

# for title, author in book_in_library:
#     book = Book(title, author)
#     library.add_book(book)

# library.list_books()
