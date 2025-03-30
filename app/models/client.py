from .book import Book


class Client:
    """This class creates a Client instance."""
    def __init__(self, ident: str, name: str, surname: str, max_allowed: int = 3, client_books: list[int] | None =
    None):
        """
        The builder instancies a client-type object to save its representative data.
        :param ident: alphanumeric code with nine elements
        :param name: client's name in string format
        :param surname: client's surname in string format
        :param max_allowed: max quantity of books in integer ('3' by default)
        """
        self.ident = ident
        self.name = name
        self.surname = surname
        self.max_allowed = max_allowed

        if client_books is None:
            self.client_books = []

        else:
            self.client_books = client_books

    def take_away(self, book: Book) -> bool:
        """
        This function changes the status-object according to different statements.
        :param book: a book-type object to interact with
        :return: None
        """
        if len(self.client_books) < self.max_allowed and book.status == "disponible":
            self.client_books.append(book.isbn)
            book.lent()
            return True

        return False

    def give_back(self, book: Book) -> bool:
        """
        This function changes the status-object according to different statements.
        :param book: a book-type object to interact with
        :return: None
        """
        if book.isbn in self.client_books:
            self.client_books.remove(book.isbn)
            book.returned()
            return True

        return False

    def save_book(self, book: Book) -> bool:
        """
        This function changes the status-object according to different statements.
        :param book: a book-type object to interact with
        :return: None
        """
        if book.isbn not in self.client_books and book.status == "prestado":
            book.saved()
            return True

        return False

    def __str__(self) -> str:
        return (
            f"<class Client("
            f"ident={repr(self.ident)}, "
            f"name={repr(self.name)}, "
            f"surname={repr(self.surname)}, "
            f"max_allowed={repr(self.max_allowed)}, "
            f"client_books={repr(self.client_books)}"
            f")>"
        )
