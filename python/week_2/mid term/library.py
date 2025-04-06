class Library:
    book_list = []

    @classmethod
    def entry_book(cls, book_id, title, author, availability):
        cls.book_list.append(Book(book_id, title, author, availability))


class Book(Library):
    def __init__(self, book_id, title, author, availability):
        self._book_id = book_id
        self._title = title
        self.__author = author
        self.__availability = availability

    @classmethod
    def borrow_book(cls, book_id):
        found = False
        for book in Library.book_list:
            if book._book_id == book_id:
                if book.__availability is True:
                    book.__availability = False
                    print("book borrowed successfully.")
                    found = True
                else:
                    print("book is already borrowed.")
                    found = True
        if not found:
            print("no book found.")

    @classmethod
    def return_book(cls,book_id):
        found = False
        for book in Library.book_list:
            if book._book_id == book_id:
                if book.__availability == True:
                    print("you didn't borrow this book")
                    found = True
                else:
                    book.__availability = True
                    print("book returned successfully.")
                    found = True
        if not found:
            print("Invalid book id.")

    @classmethod
    def all_books(cls):
        for book in Library.book_list:
            print(f"Id:{book._book_id} title:{book._title} author:{book.__author} availability:{book.__availability}")


Library.entry_book(101, "holmes", "sherlock", True)
Library.entry_book(102, "ansi c", "baverly", True)
Library.entry_book(103, "DSA", "Jennifer", True)
Library.entry_book(104, "Peripherals", "Trump", True)

while(True):
    print("\n-------------Welcome to the library------------")
    print("1. View All Books\n2. Borrow Book\n3. Return Book\n4. Exit.\n")
    n = int(input("Enter your choice: "))

    if n <= 0 or n >= 4:
        break

    if n == 1:
        Book.all_books()
    elif n == 2:
        id = int(input("book id: "))
        Book.borrow_book(id)
    elif n == 3:
        id = int(input("book id: "))
        Book.return_book(id)

 

