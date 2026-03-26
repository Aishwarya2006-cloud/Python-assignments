"""
 Create a Library Management System with the following mechanisms:

a) Design classes for Book, Member, and Library.

b) Implement methods for adding books, lending books to members, returning books, and displaying book information.

c) Create a menu-driven interface for the library management system.
   
"""

class Book:
    def __init__(self, title):
        self.title = title
        self.available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        name = input("Enter book name: ")
        b = Book(name)
        self.books.append(b)
        print("Book added successfully")

    def show_books(self):
        print("\nBooks in Library:")
        for b in self.books:
            status = "Available" if b.available else "Issued"
            print(b.title, "-", status)

    def issue_book(self):
        name = input("Enter book name to issue: ")
        for b in self.books:
            if b.title == name and b.available:
                b.available = False
                print("Book issued")
                return
        print("Book not available")

    def return_book(self):
        name = input("Enter book name to return: ")
        for b in self.books:
            if b.title == name:
                b.available = True
                print("Book returned")
                return
        print("Book not found")


lib = Library()

while True:
    print("\n1.Add Book")
    print("2.Show Books")
    print("3.Issue Book")
    print("4.Return Book")
    print("5.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        lib.add_book()
    elif ch == 2:
        lib.show_books()
    elif ch == 3:
        lib.issue_book()
    elif ch == 4:
        lib.return_book()
    elif ch == 5:
        break
    else:
        print("Invalid choice")