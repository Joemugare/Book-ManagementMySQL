# app.py
from db import create_books_table, add_book, get_all_books, delete_book

def main():
    create_books_table()

    while True:
        print("\n1. Add a Book")
        print("2. View All Books")
        print("3. Delete a Book")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            title = input("Enter the title: ")
            author = input("Enter the author: ")
            published_year = input("Enter the published year: ")

            add_book(title, author, published_year)
            print("Book added successfully!")

        elif choice == '2':
            books = get_all_books()
            print("\nList of Books:")
            for book in books:
                print(f"{book[0]}. {book[1]} by {book[2]}, Published in {book[3]}")

        elif choice == '3':
            book_id = input("Enter the ID of the book to delete: ")
            delete_book(book_id)
            print("Book deleted successfully!")

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
