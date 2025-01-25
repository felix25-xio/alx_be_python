class Book:
    def __init__(self, title, author):
       #Initialize a Book instance.
        self.title = title
        self.author = author

    def __str__(self):
    #String representation of a Book.
        return f"{self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        #Initialize an EBook instance.
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
    #String representation of an EBook.
        return f"{super().__str__()}, File Size: {self.file_size}MB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        #Initialize a PrintBook instance.
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
       #String representation of a PrintBook.
        return f"{super().__str__()}, Pages: {self.page_count}"


class Library:
    def __init__(self):
        #Initialize a Library instance with an empty list of books.
        self.books = []

    def add_book(self, book):
        #Add a book to the library.
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise TypeError("Only instances of Book or its subclasses can be added to the library.")

    def list_books(self):
        #List all books in the library.
        for book in self.books:
            print(book)

from library_system import Book, EBook, PrintBook, Library

def main():
    # Create a Library instance
    my_library = Library()

    # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books in the library
    my_library.list_books()

if __name__ == "__main__":
    main()
