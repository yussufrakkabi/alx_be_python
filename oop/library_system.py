# Base class: Book
class Book:
    def __init__(self, title, author):
        # Check for correct initialization of attributes
        if not isinstance(title, str) or not isinstance(author, str):
            raise ValueError("Title and author must be strings.")
        self.title = title
        self.author = author

    def get_info(self):
        # Return basic book information
        return f"Book: {self.title} by {self.author}"

# Derived class: EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        # Call the base class constructor
        super().__init__(title, author)
        # Check for correct initialization of the file_size attribute
        if not isinstance(file_size, int) or file_size <= 0:
            raise ValueError("File size must be a positive integer.")
        self.file_size = file_size

    def get_info(self):
        # Return EBook-specific information
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

# Derived class: PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        # Call the base class constructor
        super().__init__(title, author)
        # Check for correct initialization of the page_count attribute
        if not isinstance(page_count, int) or page_count <= 0:
            raise ValueError("Page count must be a positive integer.")
        self.page_count = page_count

    def get_info(self):
        # Return PrintBook-specific information
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

# Library class demonstrating composition
class Library:
    def __init__(self):
        self.books = []  # Initialize an empty list to store books

    def add_book(self, book):
        # Check if the object being added is an instance of Book or its derived classes
        if not isinstance(book, Book):
            raise TypeError("Can only add instances of Book or its subclasses.")
        self.books.append(book)

    def list_books(self):
        # List all books in the library
        if not self.books:
            print("The library is empty.")
        for book in self.books:
            print(book.get_info())

# Main function demonstrating usage of the classes
def main():
    # Create a Library instance
    my_library = Library()

    try:
        # Create instances of each type of book with proper checks
        classic_book = Book("Pride and Prejudice", "Jane Austen")
        digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
        paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

        # Add books to the library
        my_library.add_book(classic_book)
        my_library.add_book(digital_novel)
        my_library.add_book(paper_novel)

        # List all books in the library
        my_library.list_books()

    except (ValueError, TypeError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

