class Book:
  """
  Represents a book with title and author.
  """

  def __init__(self, title, author):
    """
    Initializes a Book object with title and author.

    Args:
        title (str): The title of the book.
        author (str): The author of the book.
    """
    self.title = title
    self.author = author

class EBook(Book):
  """
  Represents an electronic book with additional file size attribute.

  Inherits common attributes and methods from the Book class.
  """

  def __init__(self, title, author, file_size):
    """
    Initializes an EBook object by calling the Book constructor
    and adding the file_size attribute.

    Args:
        title (str): The title of the ebook.
        author (str): The author of the ebook.
        file_size (int): The file size of the ebook in KB.
    """
    super().__init__(title, author)  # Call Book constructor
    self.file_size = file_size

class PrintBook(Book):
  """
  Represents a printed book with additional page count attribute.

  Inherits common attributes and methods from the Book class.
  """

  def __init__(self, title, author, page_count):
    """
    Initializes a PrintBook object by calling the Book constructor
    and adding the page_count attribute.

    Args:
        title (str): The title of the printed book.
        author (str): The author of the printed book.
        page_count (int): The page count of the printed book.
    """
    super().__init__(title, author)  # Call Book constructor
    self.page_count = page_count

class Library:
  """
  Represents a library that manages a collection of books.

  Uses composition to hold a list of Book, EBook, and PrintBook objects.
  """

  def __init__(self):
    """
    Initializes a Library object with an empty list to store books.
    """
    self.books = []

  def add_book(self, book):
    """
    Adds a Book, EBook, or PrintBook object to the library's collection.

    Args:
        book (Book, EBook, PrintBook): The book object to add.
    """
    self.books.append(book)

  def list_books(self):
    """
    Prints details of each book in the library.

    Utilizes polymorphism to handle different book types.
    """
    print("Books in the library:")
    for book in self.books:
      # Leverage polymorphism for book type specific details
      if isinstance(book, EBook):
        print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
      elif isinstance(book, PrintBook):
        print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
      else:
        print(f"Book: {book.title} by {book.author}")
