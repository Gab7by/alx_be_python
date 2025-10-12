class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"


class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        # Call the base class (Book) constructor
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"'{self.title}' by {self.author} [EBook, {self.file_size}MB]"


class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        # Call the base class (Book) constructor
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"'{self.title}' by {self.author} [Print, {self.page_count} pages]"


class Library:
    def __init__(self):
        # Composition: Library has a list of book objects
        self.books = []

    def add_book(self, book: Book):
        # Add any instance of Book or its subclasses
        self.books.append(book)

    def list_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            print("\nBooks in the library:")
            for book in self.books:
                print(f"- {book}")
    
        
