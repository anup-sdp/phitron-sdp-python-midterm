# Phitron sdp, python midterm exam
# questions: https://docs.google.com/document/d/1FJ5VF_T2x-HmbiWDZ65cWuNbSs5f-uFst3DcvOpLPxk/edit?tab=t.0
# 4 may 2025, Anup Barua
# Library management system

class Book:
    next_id = 101  # to track next id, id starts from 101.

    def __init__(self, title, author, availability):
        self._book_id = Book.next_id
        Book.next_id += 1
        self._title = title
        self._author = author
        self.__availability = availability
        Library.entry_book(self)

    def view_book_info(self):
        if self.__availability:
            avail = 'Available'
        else:
            avail = 'Borrowed'

        print(
            f'book id: {self._book_id}, title: {self._title}, author: {self._author}, availability: {avail}')

    def borrow_book(self):
        if self.__availability:
            print(f"You have borrowed book: '{self._title}' with id : {self._book_id}.\n")
            self.__availability = False
        else:
            print(f"book: '{self._title}' with id : {self._book_id} is already borrowed, try later.\n")

    def return_book(self):
        if not self.__availability:
            self.__availability = True
            print(f"You have returned book: '{self._title}' with id : {self._book_id}.\n")
        else:
            print(f"error: book: '{self._title}' with id : {self._book_id}, is not borrowed, so you can't return it.\n")

    def get_book_id(self):
        return self._book_id


class Library:
    book_list = []

    @classmethod
    def entry_book(cls, book):
        cls.book_list.append(book)


# create some books
Book('Harry Potter', 'J.K. Rowling', True)
Book('The Hunger Games', 'Suzanne Collins', True)
Book('The Da Vinci Code', 'Dan Brown', True)
Book('A Game of Thrones', 'George R.R. Martin', True)
Book('The Kite Runner', 'Khaled Hosseini', True)

print("Welcome to Library Management System\n")


def print_menu():
    print("Menu:")
    print("1. View All Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")


def run_program():
    while True:
        print_menu()
        selected = input("Please select an option from menu : ")
        if selected == "4":
            print("Thank You for using our Library Management System app")
            break

        elif selected == "1":  # view all books
            print("All Books: ")
            # print(Library.book_list)
            for boi in Library.book_list:
                # print(boi)
                boi.view_book_info()
            print()

        elif selected == "2":  # borrow book
            try:
                seek_id = int(input("enter book id to borrow: "))
            except ValueError:
                print("Invalid input. Please enter a valid book id (integer).")
                continue
            found = False
            for boi in Library.book_list:
                if seek_id == boi.get_book_id():
                    found = True
                    boi.borrow_book()
                    break
            if not found:
                print(f"The book id: {seek_id}, is not present in database")

        elif selected == "3":  # return book
            try:
                seek_id = int(input("enter book id to return: "))
            except ValueError:
                print("Invalid input. Please enter a valid book id (integer).")
                continue
            found = False
            for boi in Library.book_list:
                if seek_id == boi.get_book_id():
                    found = True
                    boi.return_book()
                    break
            if not found:
                print(f"The book id: {seek_id}, is not present in database")

        else:
            print("invalid choice, please try again\n")


run_program()
