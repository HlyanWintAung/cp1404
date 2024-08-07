"""
Assignment 1 for CP1404/CP5632, IT@JCU

By:Hlyan Wint Aung
"""


import csv

FILENAME = 'books.csv'
MENU = """
Menu:
D - Display books
A - Add a new book
C - Complete a book
Q - Quit
>>> """


def main():
    books = load_books()
    print("Books to Read 1.0 by Hlyan Wint Aung")
    print(f"{len(books)} books loaded.\n")

    while True:
        choice = input(MENU).strip().lower()
        if choice == 'd':
            print("")
            display_books(books)
        elif choice == 'a':
            add_book(books)
        elif choice == 'c':
            complete_book(books)
        elif choice == 'q':
            save_books(books)
            print("Books saved to books.csv\n\"So many books, so little time. Frank Zappa\"")
            break
        else:
            print("Invalid menu choice\n")


def load_books():
    books = []
    try:
        with open(FILENAME, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 4:
                    title, author, pages, status = row
                    books.append([title, author, int(pages), status])
    except FileNotFoundError:
        print(f"File {FILENAME} not found. Starting with an empty list.\n")
    return books


def display_books(books):
    if not books:
        print("No books to display.\n")
    else:
        books.sort(key=lambda book: (book[1], book[0]))
        total_pages = 0
        unread_books = 0

        for i in range(len(books)):
            book = books[i]
            if book[3] == 'u':
                status = '*'
                total_pages += book[2]
                unread_books += 1
            else:
                status = ' '

            print(f"{status}{i + 1}. {book[0]:<30} by {book[1]:<20} {book[2]} pages")

        print(f"\nYou still need to read {total_pages} pages in {unread_books} books.\n")


def add_book(books):
    title = get_non_empty("Title: ")
    author = get_non_empty("Author: ")
    pages = get_variable_number("Number of Pages: ")
    books.append([title, author, pages, 'u'])
    print(f"{title} by {author} ({pages} pages) added.\n")


def complete_book(books):
    display_books(books)
    if not any(book[3] == 'u' for book in books):
        print("No unread books - well done!\n")
        return

    book_number = get_valid_book_number(len(books))
    if books[book_number - 1][3] == 'u':
        books[book_number - 1][3] = 'c'
        print(f"{books[book_number - 1][0]} by {books[book_number - 1][1]} completed!\n")
    else:
        print("That book is already completed\n")


def save_books(books):
    with open(FILENAME, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(books)


def get_non_empty(prompt):
    while True:
        response = input(prompt).strip()
        if response:
            return response
        print("Input cannot be blank\n")


def get_variable_number(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number > 0:
                return number
            print("Number must be > 0\n")
        except ValueError:
            print("Invalid input - please enter a valid number\n")


def get_valid_book_number(total_books):
    while True:
        try:
            number = int(input("Enter the number of a book to mark as completed\n>>> "))
            if 1 <= number <= total_books:
                return number
            print("Invalid book number\n")
        except ValueError:
            print("Invalid input - please enter a valid number\n")

main()