class Book:
    """A class representing a book with a title, author, and availability status."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as returned (available)."""
        self._is_checked_out = False

    def is_available(self):
        """Check if the book is available for checkout."""
        return not self._is_checked_out

class Library:
    """A class representing a library that manages a collection of books."""

    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Add a book to the library collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title if it is available."""
        for book in self._books:
            if book.title == title:
                if book.is_available():
                    book.check_out()
                    print(f"You have checked out '{title}'.")
                else:
                    print(f"Sorry, '{title}' is currently unavailable.")
                return
        print(f"Sorry, no book with the title '{title}' was found in the library.")

    def return_book(self, title):
        """Return a book by title to make it available again."""
        for book in self._books:
            if book.title == title:
                if not book.is_available():
                    book.return_book()
                    print(f"Thank you for returning '{title}'.")
                else:
                    print(f"'{title}' was not checked out.")
                return
        print(f"Sorry, no book with the title '{title}' was found in the library.")

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")
