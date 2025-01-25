class Book:
    def __init__(self, title, author, year):
        #Constructor to initialize a Book instance.
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
       # Destructor to clean up resources and print a message when an instance is deleted.
        print(f"Deleting {self.title}")

    def __str__(self):
        #String representation of the Book instance.
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        #Official representation of the Book instance, useful for debugging.
        return f"Book('{self.title}', '{self.author}', {self.year})"

from book_class import Book

def main():
    # Creating an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating the __str__ method
    print(my_book) 

    # Demonstrating the __repr__ method
    print(repr(my_book))  

    # Deleting a book instance to trigger __del__
    del my_book

if __name__ == "__main__":
    main()
