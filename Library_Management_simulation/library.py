import pickle

class Book:
    def __init__(self, book_id, title, author):
        self.book_id=book_id
        self.title=title
        self.author=author
        self.status="available"
        self.borrowed_by=None

    def __str__(self):
        return f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Status: {self.status}"

class Borrower:
    def __init__(self, borrower_id, name):
        self.borrower_id=borrower_id
        self.name=name
        self.borrowed_books=[]

    def __str__(self):
        return f"ID: {self.borrower_id}, Name: {self.name}, Books: {self.borrowed_books}"


def save_data():
    with open("library.pkl","wb") as file:
        pickle.dump((books,borrowers), file)

try:
    with open("library.pkl","rb") as file:
        books,borrowers=pickle.load(file)
except (FileNotFoundError,EOFError):
    books={}
    borrowers={}

def add_book(book_id, title, author):
    if book_id in books:
        print("Book ID already exists.")
        return
    books[book_id]=Book(book_id, title, author)
    save_data()
    print("Book added successfully.")

def remove_book(book_id):
    if book_id in books:
        if books[book_id].status=="borrowed":
            print("Cannot remove a borrowed book.")
            return
        del books[book_id]
        save_data()
        print("Book removed successfully.")
    else:
        print("Book not found.")

def add_borrower(borrower_id, name):
    if borrower_id in borrowers:
        print("Borrower ID already exists.")
        return
    borrowers[borrower_id]=Borrower(borrower_id, name)
    save_data()
    print("Borrower added successfully.")

def borrow_book(book_id, borrower_id):
    if book_id not in books:
        print("Book not found.")
        return
    if borrower_id not in borrowers:
        print("Borrower not found.")
        return

    book=books[book_id]
    borrower=borrowers[borrower_id]

    if book.status=="borrowed":
        print("Book is already borrowed.")
        return

    book.status="borrowed"
    book.borrowed_by=borrower_id
    borrower.borrowed_books.append(book_id)
    save_data()
    print("Book Borrowed Succesfully.")

def return_book(book_id):
    if book_id not in books:
        print("Book not found.")
        return

    book=books[book_id]

    if book.status=="available":
        print("Book is already available.")
        return

    borrower_id=book.borrowed_by
    borrower=borrowers[borrower_id]

    book.status="available"
    book.borrowed_by=None
    borrower.borrowed_books.remove(book_id)
    save_data()
    print("Book returned successfully.")

def display_books():
    if not books:
        print("No books in catalog.")
        return
    for book in books.values():
        print(book)

def display_borrowers():
    if not borrowers:
        print("No borrowers registered.")
        return
    for borrower in borrowers.values():
        print(borrower)


while True:
    print("options:")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Add Borrower")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Display Books")
    print("7. Display Borrowers")
    print("8. quit")

    choice=input("Enter your choice: ")

    if choice=="1":
        book_id=input("Book ID: ")
        title=input("Title: ")
        author=input("Author: ")
        add_book(book_id, title, author)

    elif choice=="2":
        book_id=input("Book ID to remove: ")
        remove_book(book_id)

    elif choice == "3":
        borrower_id = input("Borrower ID: ")
        name = input("Borrower Name: ")
        add_borrower(borrower_id, name)

    elif choice == "4":
        book_id = input("Book ID: ")
        borrower_id = input("Borrower ID: ")
        borrow_book(book_id, borrower_id)

    elif choice == "5":
        book_id = input("Book ID: ")
        return_book(book_id)

    elif choice == "6":
        display_books()

    elif choice == "7":
        display_borrowers()

    elif choice=="8":
        print("Exiting program.")
        break

    else:
        print("Invalid option. Please try again.")