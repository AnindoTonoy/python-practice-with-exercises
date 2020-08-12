# A library management system
# create a library class
# display books
# add books
# lend books - (who owns the books if not present)
# return books

# AnindoLibrary = Library (listofbooks, library_name)
# dictionary (key: books, value: name of person)
# Create a main function and run an infinite loop asking user for input
# --------------------------------------------------------------------------

import sys


class Library:

    def __init__(self, list_of_books, library_name):
        self.list_of_books = list_of_books
        self.library_name = library_name
        self.lend_data = {}

    # Display list of books
    def display_books(self):
        print('|| Available books are:')
        for count, book in enumerate(self.list_of_books, 1):
            print(f'{count}.  {book}')

    # Add new book to the list
    def add_books(self, new_book):
        # Append the book in the list of books
        self.list_of_books.append(new_book)
        print(f'"{new_book}" is  added to the list.\n')

    # lend book from the list
    def lend_books(self, lender_name, lending_book):
        # Checking the book is in book-list or not
        if lending_book in self.list_of_books:
            # Checking the book is in lend data or not
            if lending_book in self.lend_data:
                print(f'Sorry! This book is lend by {self.lend_data[lending_book]}.\n')

            else:
                self.lend_data[lending_book] = lender_name
                print('Book lend.')

        else:
            print('Sorry! you entered the wrong book name.')

    # Return lend book to the list
    def return_books(self, lending_book):
        if lending_book in self.lend_data:
            print(f'Lend details:\nThis book is lend by {self.lend_data[lending_book]}.\n'
                  f'Do you want to return this book? if Yes enter "y" or for skip press any key.')
            r_input = input('Enter: ')

            if r_input == 'y':
                del self.lend_data[lending_book]
                print('Thank you for returning this book.\n')

            else:
                pass

        else:
            print('Sorry! you entered the wrong book name.')


def main_f():
    # By deafault variables
    list_of_books = ["C", "C++", "Python", "Java", "JavaScript", "Rubi"]
    library_name = "Anindo's Library"

    library = Library(list_of_books, library_name)

    print(f'\n============| Welcome to {library.library_name} |============\n')

    while True:
        print('\n\t\t\t++++| Main menu |++++')
        print('- For view the available books enter "d"\n- For lend books enter "l"\n'
              '- For return books enter "r"\n- For add books enter "a"\n- For exit enter "q"')
        _input = input("Please Enter your input here: ")

        if _input == "q":
            print('\nThank you for using this system.')
            sys.exit()

        elif _input == "d":
            library.display_books()

            # Main menu or exit
            mm_input = input("For continuing with main menu enter 'c' or "
                             "exit enter 'q'\nEnter: ")

            if mm_input == 'c':
                continue
            elif mm_input == 'q':
                print('\nThank you for using this system.')
                sys.exit()

        elif _input == "l":
            l_name = input('Enter your name: ')
            l_book = input('Enter book name you want to lend: ')
            library.lend_books(l_name, l_book)

            # Main menu or exit
            mm_input = input("For continuing with main menu enter 'c' or "
                             "exit enter 'q'\nEnter: ")

            if mm_input == 'c':
                continue
            elif mm_input == 'q':
                print('\nThank you for using this system.')
                sys.exit()

        elif _input == "r":
            r_book = input('Enter the book name which you want to return: ')
            library.return_books(r_book)

        elif _input == "a":
            add = input('Add the book to the Book lists:\n')
            library.add_books(add)

            mm_input = input("For continuing with main menu enter 'c' or "
                             "exit enter 'q'\nEnter: ")

            if mm_input == 'c':
                continue
            elif mm_input == 'q':
                print('\nThank you for using this system.')
                sys.exit()


if __name__ == '__main__':
    main_f()
